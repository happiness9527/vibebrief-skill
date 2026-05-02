# Milestone Report Example

## Input

Fictional project: TutorFlow.

```text
The onboarding form now saves a learner profile, the dashboard loads the saved profile,
and the agent showed a passing smoke test for signup-to-dashboard.
```

## VibeBrief Output

**Milestone name:** First learner onboarding loop.

**Stage goal:** Let a learner create a basic profile and see it on the dashboard.

**Completed capability:**

- Learner profile data can be saved.
- Dashboard can read and display the saved profile.
- A smoke test covers the signup-to-dashboard path.

**Key decisions:**

- Keep the first profile simple.
- Verify the end-to-end learner path before adding more profile fields.

**Current stable capability:**

- The basic onboarding loop appears stable if the smoke test result is accurate.

**Verified:**

- Signup-to-dashboard smoke test passed, based on the provided summary.

**Unclosed risks:**

- No evidence yet for browser compatibility or error states.
- No evidence yet for empty or invalid profile data.

**Snapshot recommendation:** Save snapshot.

**Next-stage boundary:**

- Add basic validation and error messages only.

**Do not expand yet:**

- Do not add payments, notifications, or advanced analytics in the next stage.

**Prompt for the next AI:**

```text
We have a stable TutorFlow milestone: basic learner onboarding to dashboard.
Next, add only basic validation and clear error messages for the onboarding form.
Keep the existing smoke test passing and show the test result before claiming completion.
```
