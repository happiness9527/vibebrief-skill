# Contributing

Thanks for helping improve VibeBrief.

## Project Scope

VibeBrief is a skill for turning AI coding sessions into plain-language briefs, visual summaries, milestone reports, handoff packs, and reusable project memory.

Please keep contributions aligned with that scope. VibeBrief is not a coding agent, code review system, UI product, or background automation service.

## Good Contributions

- Clearer briefing templates for non-engineers
- Better examples using fictional projects
- Safer project memory rules
- More practical Mermaid visual patterns
- Improvements to the lightweight helper scripts
- Documentation for installing VibeBrief in different local skill systems

## Before Opening A Pull Request

Run:

```bash
python3 vibebrief/scripts/doctor.py
python3 -m py_compile vibebrief/scripts/*.py
git diff --check
```

Do not include private company names, customer data, credentials, internal paths, or real project logs.

## Style

- Use plain language.
- Explain project meaning, not only file changes.
- Mark unverified claims as unverified.
- Keep examples fictional.
- Prefer small, reviewable changes.
