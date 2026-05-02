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

Important product, technical, or workflow decisions.

### risks/

Open risks, unverified claims, and acceptance gaps.

### handoff/

Prompt-ready packages for new AI chats or different agents.

### visuals/

Mermaid diagrams and short explanations.

### index.json

A generated index of memory records.

## Privacy

Public repositories should not include private worklogs. Put sensitive notes in `docs/ai-worklog/private/`, which is ignored by this repository's `.gitignore`.
