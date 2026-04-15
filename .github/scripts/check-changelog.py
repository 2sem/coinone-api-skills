#!/usr/bin/env python3
"""Check Coinone API changelog RSS for new entries.

State stored in GitHub issues (label: api-update) — no repo commits for state.
Outputs to GITHUB_OUTPUT:
  status=HAS_UPDATES | NO_UPDATES | FIRST_RUN
  latest_title=<title>
  latest_date=<RFC2822 date>
"""

import json
import os
import ssl
import sys
import urllib.request
import xml.etree.ElementTree as ET

RSS_URL = "https://docs.coinone.co.kr/changelog.rss"
GITHUB_OUTPUT = os.environ.get("GITHUB_OUTPUT", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "")


def fetch_rss() -> ET.Element:
    req = urllib.request.Request(RSS_URL, headers={"User-Agent": "coinone-api-monitor/1.0"})
    # SKIP_SSL_VERIFY=1 for local macOS dev only — never set in CI
    ctx = ssl._create_unverified_context() if os.environ.get("SKIP_SSL_VERIFY") else None
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        return ET.fromstring(resp.read())


def latest_rss_entry(root: ET.Element) -> tuple[str, str]:
    item = root.find(".//item")
    if item is None:
        raise ValueError("No items in RSS feed")
    title = (item.findtext("title") or "").strip()
    pub_date = (item.findtext("pubDate") or "").strip()
    return title, pub_date


def get_last_known_date() -> str:
    """Read pubDate from latest api-update issue body."""
    if not GITHUB_TOKEN or not GITHUB_REPOSITORY:
        print("[check] No GITHUB_TOKEN/REPOSITORY — treating as FIRST_RUN", file=sys.stderr)
        return ""

    url = (
        f"https://api.github.com/repos/{GITHUB_REPOSITORY}/issues"
        "?labels=api-update&state=all&per_page=1&sort=created&direction=desc"
    )
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            issues = json.loads(resp.read())
    except Exception as e:
        print(f"[check] GitHub API error: {e} — treating as FIRST_RUN", file=sys.stderr)
        return ""

    if not issues:
        return ""

    body = issues[0].get("body", "")
    for line in body.splitlines():
        if line.startswith("**pubDate:**"):
            return line.split(":", 1)[1].strip()

    return ""


def write_output(key: str, value: str) -> None:
    print(f"{key}={value}")
    if GITHUB_OUTPUT:
        with open(GITHUB_OUTPUT, "a", encoding="utf-8") as f:
            f.write(f"{key}={value}\n")


def main() -> None:
    root = fetch_rss()
    title, pub_date = latest_rss_entry(root)

    print(f"[check] Latest RSS: {title!r} ({pub_date})", file=sys.stderr)

    last_known = get_last_known_date()
    print(f"[check] Last known: {last_known!r}", file=sys.stderr)

    write_output("latest_title", title)
    write_output("latest_date", pub_date)

    if not last_known:
        write_output("status", "FIRST_RUN")
    elif pub_date != last_known:
        write_output("status", "HAS_UPDATES")
    else:
        write_output("status", "NO_UPDATES")


if __name__ == "__main__":
    main()
