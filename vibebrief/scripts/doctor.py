#!/usr/bin/env python3
"""Check the VibeBrief repository before publishing."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    ".gitignore",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/ISSUE_TEMPLATE/use_case.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "vibebrief/SKILL.md",
    "vibebrief/references/intent-router.md",
    "vibebrief/references/output-templates.md",
    "vibebrief/references/session-brief-rules.md",
    "vibebrief/references/milestone-report-rules.md",
    "vibebrief/references/handoff-pack-rules.md",
    "vibebrief/references/visual-summary-rules.md",
    "vibebrief/references/project-memory-rules.md",
    "vibebrief/references/acceptance-mode-rules.md",
    "vibebrief/references/project-profile-template.md",
    "vibebrief/examples/session-brief-example.md",
    "vibebrief/examples/milestone-report-example.md",
    "vibebrief/examples/handoff-pack-example.md",
    "vibebrief/examples/visual-summary-example.md",
    "vibebrief/examples/project-memory-example.md",
    "vibebrief/examples/acceptance-mode-example.md",
    "vibebrief/scripts/collect_context.py",
    "vibebrief/scripts/write_memory.py",
    "vibebrief/scripts/update_index.py",
    "vibebrief/scripts/doctor.py",
    "docs/install.md",
    "docs/quick-start-for-non-engineers.md",
    "docs/use-cases.md",
    "docs/how-it-works.md",
    "docs/memory-structure.md",
    "docs/github-publish-guide.md",
    "docs/roadmap.md",
    "demo/before.md",
    "demo/after.md",
]

REQUIRED_DIRS = [
    "vibebrief/references",
    "vibebrief/examples",
    "vibebrief/scripts",
    "docs",
    "demo/sample-ai-worklog",
]

REQUIRED_GITIGNORE_LINES = [
    ".env",
    "*.local",
    "project-profile.local.md",
    "docs/ai-worklog/private/",
    "node_modules/",
    "__pycache__/",
]

LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(?:password|token|api[_-]?key|secret)\s*[:=]\s*['\"][^'\"\s]{8,}['\"]"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_required_files(errors: list[str]) -> None:
    for item in REQUIRED_FILES:
        path = ROOT / item
        if not path.is_file():
            errors.append(f"Missing file: {item}")
    for item in REQUIRED_DIRS:
        path = ROOT / item
        if not path.is_dir():
            errors.append(f"Missing directory: {item}")


def check_skill_frontmatter(errors: list[str]) -> None:
    path = ROOT / "vibebrief" / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md is missing YAML frontmatter.")
        return
    frontmatter = match.group(1)
    expected = [
        "name: vibebrief",
        "description: Use this skill when a non-engineer needs to understand, summarize, visualize, or preserve an AI coding session, create a milestone report, generate a handoff pack, or turn messy AI coding conversations into reusable project memory.",
        "metadata:",
        "  short-description: Turn AI coding sessions into clear briefs, visual summaries, and reusable project memory.",
    ]
    for line in expected:
        if line not in frontmatter:
            errors.append(f"SKILL.md frontmatter missing: {line}")


def check_readme_links(errors: list[str]) -> None:
    markdown_files = [ROOT / "README.md", ROOT / "README.zh-CN.md"]
    markdown_files.extend(sorted((ROOT / "docs").glob("*.md")))
    for markdown_file in markdown_files:
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.strip("<>")
            target = target.split("#", 1)[0]
            if not target:
                continue
            candidate = (markdown_file.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"Link leaves repository in {rel(markdown_file)}: {raw_target}")
                continue
            if not candidate.exists():
                errors.append(f"Broken link in {rel(markdown_file)}: {raw_target}")


def check_markdown_lines(errors: list[str]) -> None:
    for markdown_file in sorted(ROOT.rglob("*.md")):
        in_code = False
        in_frontmatter = False
        for number, line in enumerate(markdown_file.read_text(encoding="utf-8").splitlines(), start=1):
            stripped = line.strip()
            if number == 1 and stripped == "---":
                in_frontmatter = True
                continue
            if in_frontmatter:
                if stripped == "---":
                    in_frontmatter = False
                continue
            if stripped.startswith("```") or stripped.startswith("````"):
                in_code = not in_code
            if in_code or "http://" in line or "https://" in line:
                continue
            if len(line) > 240:
                errors.append(f"Long Markdown line in {rel(markdown_file)}:{number}")


def check_privacy_risks(errors: list[str]) -> None:
    risky_names = {".env", ".npmrc", ".pypirc", "id_rsa", "id_ed25519"}
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file() and path.name in risky_names:
            errors.append(f"Risky private file name present: {rel(path)}")
        if path.is_file() and path.suffix in {".pem", ".key"}:
            errors.append(f"Risky private key-like file present: {rel(path)}")
        if path.is_file() and path.suffix.lower() in {".md", ".py", ".json", ".yml", ".yaml", ".txt"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    errors.append(f"Possible secret pattern in {rel(path)}")
                    break


def check_gitignore(errors: list[str]) -> None:
    lines = set((ROOT / ".gitignore").read_text(encoding="utf-8").splitlines())
    for line in REQUIRED_GITIGNORE_LINES:
        if line not in lines:
            errors.append(f".gitignore missing required entry: {line}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_skill_frontmatter(errors)
    check_readme_links(errors)
    check_markdown_lines(errors)
    check_privacy_risks(errors)
    check_gitignore(errors)

    if errors:
        print("VibeBrief doctor found problems:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VibeBrief doctor passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
