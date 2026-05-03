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

Default to generating memory content first. Do not write files unless the user explicitly asks to save, write, or preserve.

Before writing, show the target path. Never silently write private project details. If sensitive information appears, summarize or redact it.

When writing public records, keep them short, sanitized, and useful for future handoff.
