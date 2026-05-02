#!/usr/bin/env python3
"""Collect lightweight context for a VibeBrief session."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


def run_command(command: list[str], cwd: Path) -> dict[str, Any]:
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except FileNotFoundError:
        return {"ok": False, "output": f"{command[0]} not found"}
    except subprocess.TimeoutExpired:
        return {"ok": False, "output": "command timed out"}

    output = (completed.stdout + completed.stderr).strip()
    return {
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "output": output or "(no output)",
    }


def read_optional(path: Path, max_chars: int = 6000) -> dict[str, Any]:
    if not path.exists():
        return {"exists": False, "content": ""}
    if not path.is_file():
        return {"exists": False, "content": ""}
    content = path.read_text(encoding="utf-8", errors="replace")
    if len(content) > max_chars:
        content = content[:max_chars] + "\n\n[truncated]"
    return {"exists": True, "content": content}


def collect(root: Path) -> dict[str, Any]:
    worklog = root / "docs" / "ai-worklog"
    return {
        "root": str(root),
        "git": {
            "status": run_command(["git", "status", "--short"], root),
            "diff_stat": run_command(["git", "diff", "--stat"], root),
            "recent_log": run_command(["git", "log", "-5", "--oneline"], root),
        },
        "memory": {
            "current_status": read_optional(worklog / "current-status.md"),
            "latest_handoff": read_optional(worklog / "handoff" / "latest-handoff.md"),
        },
    }


def print_markdown(data: dict[str, Any]) -> None:
    print("# VibeBrief Context Snapshot")
    print()
    print(f"Root: `{data['root']}`")
    print()
    print("## Git Status")
    print()
    print("```text")
    print(data["git"]["status"]["output"])
    print("```")
    print()
    print("## Git Diff Stat")
    print()
    print("```text")
    print(data["git"]["diff_stat"]["output"])
    print("```")
    print()
    print("## Recent Git Log")
    print()
    print("```text")
    print(data["git"]["recent_log"]["output"])
    print("```")
    print()

    current = data["memory"]["current_status"]
    handoff = data["memory"]["latest_handoff"]
    print("## Current Status Memory")
    print()
    print(current["content"] if current["exists"] else "No current-status.md found.")
    print()
    print("## Latest Handoff Memory")
    print()
    print(handoff["content"] if handoff["exists"] else "No latest handoff found.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect lightweight VibeBrief context.")
    parser.add_argument("--root", default=".", help="Project root to inspect.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    data = collect(root)
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print_markdown(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
