# Confidence Check Example

## Input

Fictional project: TutorFlow.

```text
The AI says the dashboard crash is fixed. It only said "I updated the null check,
so it should work now."
```

## Possible VibeBrief Output

Confidence is low.

The AI described a likely code change, but did not show proof that the original crash path now works.

Minimum next check: reproduce the dashboard path that crashed before and show the result.
