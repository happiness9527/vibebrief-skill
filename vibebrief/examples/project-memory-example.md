# Project Memory Example

## User Request

```text
Help me save this session as local project memory.
```

## VibeBrief Should Generate First

```markdown
# Session: DemoDesk workspace sync fix

Date: 2026-05-02
Mode: Session Brief
Source status: AI-provided summary
Verification status: Unverified

## Summary

The AI says it fixed the workspace window sync problem by changing the web entry file and controller.

## Project Meaning

If verified, this improves the stability of the main workspace startup flow.

## Verified

No direct evidence was provided.

## Risks

The app may still fail on fresh startup.

## Next Action

Run `/workspace` and provide the result before adding new features.
```

## Suggested Write Paths

- `docs/ai-worklog/sessions/2026-05-02-demodesk-workspace-sync-fix.md`
- `docs/ai-worklog/current-status.md`
- `docs/ai-worklog/index.json`

VibeBrief V0.1 should ask before writing unless the user already gave clear write permission.
