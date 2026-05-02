#!/usr/bin/env python3
"""Write VibeBrief artifacts into docs/ai-worklog."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


CATEGORIES = {
    "session": "sessions",
    "milestone": "milestones",
    "decision": "decisions",
    "risk": "risks",
    "handoff": "handoff",
    "visual": "visuals",
}


README_TEXT = """# AI Worklog

This directory stores VibeBrief project memory.

Keep public records sanitized. Put private notes under `private/`, which should be ignored by Git.
"""


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value[:60] or "entry"


def read_content(args: argparse.Namespace) -> str:
    if args.content_file:
        return Path(args.content_file).read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("No content provided. Pass --content-file or pipe Markdown through stdin.")


def ensure_worklog(root: Path) -> Path:
    worklog = root / "docs" / "ai-worklog"
    for directory in ["sessions", "milestones", "decisions", "risks", "handoff", "visuals", "private"]:
        (worklog / directory).mkdir(parents=True, exist_ok=True)
    readme = worklog / "README.md"
    if not readme.exists():
        readme.write_text(README_TEXT, encoding="utf-8")
    return worklog


def write_memory(args: argparse.Namespace) -> Path:
    root = Path(args.root).resolve()
    worklog = ensure_worklog(root)
    category_dir = worklog / CATEGORIES[args.type]
    content = read_content(args).strip() + "\n"
    date = args.date or datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%H%M%S")
    filename = f"{date}-{timestamp}-{slugify(args.title)}.md"
    output_path = category_dir / filename

    if args.dry_run:
        print(content)
        return output_path

    output_path.write_text(content, encoding="utf-8")

    if args.write_current_status:
        (worklog / "current-status.md").write_text(content, encoding="utf-8")

    if args.type == "handoff":
        (worklog / "handoff" / "latest-handoff.md").write_text(content, encoding="utf-8")

    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a VibeBrief memory artifact.")
    parser.add_argument("--root", default=".", help="Project root where docs/ai-worklog should live.")
    parser.add_argument("--type", choices=sorted(CATEGORIES), required=True, help="Memory record type.")
    parser.add_argument("--title", required=True, help="Short title for the record.")
    parser.add_argument("--date", help="Record date in YYYY-MM-DD format. Defaults to today.")
    parser.add_argument("--content-file", help="Markdown file to write. Defaults to stdin.")
    parser.add_argument("--write-current-status", action="store_true", help="Also update current-status.md.")
    parser.add_argument("--dry-run", action="store_true", help="Print content without writing files.")
    args = parser.parse_args()

    output_path = write_memory(args)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
