# Session Brief Rules

Session Brief is the default mode when a user wants to understand one AI coding session.

## Required Sections

- Session goal
- What the AI actually did
- Why it likely did this
- Key files or modules
- Product or project meaning of each important change
- Verified items
- Unverified items
- Current risks
- Current project stage
- Next step
- Copy-paste prompt for the next AI

## Interpretation Rules

- Translate technical actions into user-facing meaning.
- If a file name is mentioned, explain why that file probably matters.
- If the AI says "should work", treat it as a claim, not proof.
- If no command output, screenshot, test result, or manual check is present, mark the item unverified.
- If the session includes too many directions, recommend narrowing the next turn.

## Evidence Labels

Use these labels consistently:

- Changed: the AI says it modified something.
- Verified: there is direct evidence from a command, test, screenshot, log, or user confirmation.
- Unverified: the change is claimed but not proven.
- Risk: a likely failure point or decision that may cause rework.
- Safe to continue: enough evidence exists for the next step.
- Not recommended to continue: key evidence is missing.

## Tone

Write for a smart non-engineer. Avoid jargon when a simple phrase works.
