# Installation

VibeBrief is a local skill folder. The core installable unit is `vibebrief/`.

## Recommended Path

Ask your AI coding agent to install it:

```text
Please install this repository as a local skill named vibebrief:
https://github.com/happiness9527/vibebrief-skill
Use the vibebrief/ directory as the skill folder.
Keep the directory name and skill name as vibebrief.
After installing, confirm where SKILL.md was placed.
```

If you fork this project, replace the URL with your actual repository.

## Manual Install

1. Clone or download this repository.
2. Copy `vibebrief/` into the skills directory used by your AI coding tool.
3. Restart or refresh the tool if required.
4. Ask: "Use VibeBrief to summarize this AI coding session."

## What If `/vibebrief` Is Not Recognized?

Some AI tools use different local skill directories, instruction folders, or command registration systems.

If `/vibebrief` is not recognized after installation, VibeBrief can still be used.

If `/vibebrief` returns `Unknown command` after installation, fully exit and restart Claude Code. Newly installed local skills are usually detected in a new session.

Start with the prompt in [Try Without Installing](../README.md#try-without-installing), or ask your current AI tool to explain which local instruction or skill installation format it supports.

## Verify The Repository

From the repository root:

```bash
python3 vibebrief/scripts/doctor.py
python3 -m py_compile vibebrief/scripts/*.py
```

## What Not To Install

Do not install `demo/` or `docs/` as part of the skill unless your tool expects the whole repository. The skill itself lives in `vibebrief/`.
