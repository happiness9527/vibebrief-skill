# Acceptance Mode Example

## Input

Fictional project: TutorFlow.

```text
The AI says the dashboard crash is fixed. It only said "I updated the null check,
so it should work now."
```

## VibeBrief Output

**Completion confidence:** Low.

**What appears changed:**

- The AI says it added or changed a null check.

**Evidence available:**

- Only the AI's claim is available.

**Evidence missing:**

- No command output.
- No test result.
- No screenshot.
- No reproduction of the original crash.

**Minimum acceptance action:**

- Reproduce the dashboard path that crashed before.
- Show that the dashboard now loads with the same data or empty state.

**Should continue?** Not yet.

**Next question to ask the AI:**

```text
Before continuing, please prove the dashboard crash fix.
Reproduce the original dashboard path, show the exact command or manual action,
show the result, and state what remains untested.
Do not add new dashboard features until this is verified.
```
