#!/usr/bin/env python3
"""Update docs/ai-worklog/index.json."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


CATEGORY_DIRS = {
    "session": "sessions",
    "milestone": "milestones",
    "decision": "decisions",
    "risk": "risks",
    "handoff": "handoff",
    "visual": "visuals",
}


def title_from_markdown(path: Path) -> str:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").strip()


def build_index(root: Path) -> dict[str, object]:
    worklog = root / "docs" / "ai-worklog"
    entries: list[dict[str, object]] = []
    for record_type, directory in CATEGORY_DIRS.items():
        folder = worklog / directory
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            stat = path.stat()
            entries.append(
                {
                    "type": record_type,
                    "title": title_from_markdown(path),
                    "path": path.relative_to(root).as_posix(),
                    "updated_at": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
                }
            )

    return {
        "schema_version": 1,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "entries": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Update VibeBrief memory index.")
    parser.add_argument("--root", default=".", help="Project root where docs/ai-worklog lives.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    worklog = root / "docs" / "ai-worklog"
    worklog.mkdir(parents=True, exist_ok=True)
    index = build_index(root)
    output_path = worklog / "index.json"
    output_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {output_path} with {len(index['entries'])} entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
