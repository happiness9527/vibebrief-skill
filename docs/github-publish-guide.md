# GitHub Publish Guide

This guide prepares VibeBrief for publishing as `vibebrief-skill`.

## Before Publishing

Run from the repository root:

```bash
python3 vibebrief/scripts/doctor.py
python3 -m py_compile vibebrief/scripts/*.py
git diff --check
```

Review the output manually.

## Privacy Review

Confirm the repository does not contain:

- Real company names
- Real customer data
- Internal project paths
- API keys or access tokens
- Passwords or private keys
- Private AI coding transcripts

Examples should use fictional projects such as TutorFlow, DemoDesk, SoloCRM, or CoursePilot.

## Suggested Repository Settings

- Repository name: `vibebrief-skill`
- Visibility: public
- License: MIT
- Default branch: `main`
- Issues: enabled
- Discussions: optional

## First Release Checklist

- [ ] README.md is complete.
- [ ] README.zh-CN.md is complete.
- [ ] `vibebrief/SKILL.md` has valid frontmatter.
- [ ] Examples cover the six V0.1 modes.
- [ ] `doctor.py` passes.
- [ ] Scripts compile.
- [ ] No private data is included.

## Publish Commands

Use your preferred GitHub workflow. One possible sequence is:

```bash
git init
git add .
git commit -m "Initial VibeBrief skill"
git branch -M main
git remote add origin git@github.com:YOUR_NAME/vibebrief-skill.git
git push -u origin main
```

Only run these commands when you are ready to publish.
