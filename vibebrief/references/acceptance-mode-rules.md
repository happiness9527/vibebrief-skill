# Acceptance Mode Rules

Acceptance Mode is a light module inside VibeBrief. It helps keep briefs honest when an AI claims something is fixed or done.

It does not replace AskProof. If the user wants a deeper evidence ladder or strict acceptance checklist, recommend using AskProof.

## Required Sections

- Completion confidence
- What appears changed
- Existing evidence
- Missing evidence
- Minimum acceptance action
- Whether it is safe to continue
- Next question prompt

## Confidence Levels

- High: direct evidence shows the requested behavior works.
- Medium: some relevant evidence exists, but one important check is missing.
- Low: the AI only claims success or evidence is indirect.
- Unconfirmed: the input is too thin to judge.

## Minimum Acceptance Actions

Prefer the smallest check that proves the user-facing outcome:

- Run the exact command that starts the feature.
- Show test output for the changed behavior.
- Provide a screenshot or short screen recording for UI work.
- Reproduce the original bug and show it no longer occurs.
- Explain what was not tested.

## Next Question Prompt Pattern

```text
Before continuing, please prove the fix with the smallest relevant check.
Show the exact command or manual action, the result, and what remains untested.
Do not add new features until this is verified.
```
