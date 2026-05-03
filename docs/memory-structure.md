# Memory Structure

VibeBrief uses `docs/ai-worklog/` as the default local memory location.

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

## Files

### README.md

Explains what the worklog is and how to treat private notes.

### current-status.md

The latest known project state in plain language.

### sessions/

One Session Brief per important coding session.

### milestones/

Stage-level reports that mark possible checkpoints.

### decisions/

Short decision notes.

### risks/

Open risks or uncertainty notes.

### handoff/

Compact handoff notes for new AI chats.

### visuals/

Mermaid diagrams and short explanations.

### index.json

A lightweight generated index.

## Privacy

Public repositories should not include private worklogs. Put sensitive notes in `docs/ai-worklog/private/`, which is ignored by this repository's `.gitignore`.
