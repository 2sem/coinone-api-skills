#!/usr/bin/env python3
"""Pre-check if changelog entry is likely already documented.

Extracts distinctive terms from entry title, greps references/.
Outputs to GITHUB_OUTPUT:
  skip=true   — terms found, Claude not needed
  skip=false  — not found, invoke Claude
  target_file — most relevant file for Claude to check
"""

import os
import re
import subprocess
import sys

# Specific Korean nouns → English API terms
# Generic words (주문, 지원, 안내) excluded intentionally
KOREAN_TO_EN = {
    '웹소켓': 'websocket',
    '차트': 'chart',
    '리워드': 'reward',
    '보상': 'reward',
    '포트폴리오': 'portfolio',
    '부분취소': 'partial',
    '호가단위': 'range_unit',
    '호가 단위': 'range_unit',
    '출금': 'withdrawal',
    '입금': 'deposit',
    '수수료': 'fee',
    '잔고': 'balance',
    '잔액': 'balance',
    '티커': 'ticker',
}

# Map terms to the most relevant reference file
TERM_TO_FILE = {
    'websocket': 'references/websocket.md',
    'chart': 'references/websocket.md',
    'order': 'references/private-rest-v21.md',
    'cancel': 'references/private-rest-v21.md',
    'balance': 'references/private-rest-v21.md',
    'withdrawal': 'references/private-rest-v21.md',
    'deposit': 'references/private-rest-v21.md',
    'reward': 'references/private-rest-v21.md',
    'portfolio': 'references/private-rest-v21.md',
    'fee': 'references/private-rest-v21.md',
    'partial': 'references/private-rest-v21.md',
    'ticker': 'references/public-rest-v2.md',
    'orderbook': 'references/public-rest-v2.md',
    'trade': 'references/public-rest-v2.md',
    'currency': 'references/public-rest-v2.md',
    'market': 'references/public-rest-v2.md',
    'range_unit': 'references/public-rest-v2.md',
}


_GENERIC = {'api', 'url', 'get', 'put', 'post', 'rest', 'http', 'json', 'v1', 'v2'}


def extract_terms(title: str) -> list[str]:
    terms = []

    # Uppercase API tokens are most distinctive (STOP_LIMIT, UUID, KRW, CHART)
    for t in re.findall(r'[A-Z][A-Z_]{2,}', title):
        lower = t.lower()
        if lower not in _GENERIC:
            terms.append(lower)

    # Known Korean nouns → English equivalent
    for kr, en in KOREAN_TO_EN.items():
        if kr in title:
            terms.append(en)

    return list(set(terms))


def grep_references(term: str) -> bool:
    result = subprocess.run(
        ['grep', '-ri', term, 'references/', '--include=*.md', '-q'],
        capture_output=True,
    )
    return result.returncode == 0


def write_output(key: str, value: str) -> None:
    print(f"{key}={value}")
    github_output = os.environ.get('GITHUB_OUTPUT', '')
    if github_output:
        with open(github_output, 'a', encoding='utf-8') as f:
            f.write(f"{key}={value}\n")


def main() -> None:
    title = os.environ.get('ENTRY_TITLE', '')
    if not title and len(sys.argv) > 1:
        title = sys.argv[1]

    if not title:
        write_output('skip', 'false')
        write_output('target_file', '')
        return

    terms = extract_terms(title)
    print(f"[pre-grep] Title: {title!r}", file=sys.stderr)
    print(f"[pre-grep] Terms: {terms}", file=sys.stderr)

    if not terms:
        # No distinctive terms extracted — let Claude decide
        write_output('skip', 'false')
        write_output('target_file', '')
        return

    found = [t for t in terms if grep_references(t)]
    missing = [t for t in terms if t not in found]
    print(f"[pre-grep] Found: {found}, Missing: {missing}", file=sys.stderr)

    # Determine target file from first matched term
    target_file = next(
        (TERM_TO_FILE[t] for t in terms if t in TERM_TO_FILE), ''
    )
    write_output('target_file', target_file)

    # Skip Claude if ALL distinctive terms already documented
    if found and not missing:
        print('[pre-grep] All terms found — skip Claude', file=sys.stderr)
        write_output('skip', 'true')
    else:
        print('[pre-grep] Terms missing — invoke Claude', file=sys.stderr)
        write_output('skip', 'false')


if __name__ == '__main__':
    main()
