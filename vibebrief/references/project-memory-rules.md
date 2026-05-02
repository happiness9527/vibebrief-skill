# Project Memory Rules

Project Memory turns useful VibeBrief output into local records.

## Default Directory

```text
docs/ai-worklog/
├── README.md
├── current-status.md
├── sessions/
├── milestones/
├── decisions/
├── risks/
├── handoff/
├── visuals/
└── index.json
```

## Write Behavior

V0.1 should generate content and ask before writing files unless the user explicitly says to write.

Default behavior:

- Generate memory content first.
- Do not write files unless the user explicitly asks to save, write, or preserve.
- Before writing, show the target path.
- Never silently write private project details.
- If sensitive information appears, summarize or redact it.

When writing:

- Keep sensitive notes out of public files.
- Use fictional or generalized names in examples.
- Store private notes under `docs/ai-worklog/private/`, which should be ignored by Git.
- Update `current-status.md` when the session changes the known project state.
- Run `update_index.py` after adding new records.

## Suggested Record Types

- `sessions/`: one coding session brief
- `milestones/`: stage-level report
- `decisions/`: key product or technical decisions
- `risks/`: unresolved risks and verification gaps
- `handoff/`: new-chat or new-agent handoff packs
- `visuals/`: Mermaid diagrams and explanations

## Minimum Metadata

Each saved file should include:

- Title
- Date
- Mode
- Source status: user-provided, AI-provided, or unconfirmed
- Verification status
- Next action
