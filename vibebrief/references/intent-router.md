# Intent Router

VibeBrief should infer the mode from the user's natural language. Do not force users to memorize commands.

## Routing Table

| User intent | Route to | Typical phrases |
| --- | --- | --- |
| Understand a finished coding session | Session Brief | "summarize this session", "what did the AI do", "I don't understand this change" |
| Decide whether a stage is complete | Milestone Report | "is this a milestone", "stage summary", "stable checkpoint" |
| Start a new chat or switch AI agents | Handoff Pack | "new chat", "context loss", "handoff", "give this to Codex" |
| Understand with a diagram | Visual Summary | "draw this", "use Mermaid", "show the flow" |
| Save process records locally | Project Memory | "save this", "write worklog", "project memory" |
| Check a completion claim | Acceptance Mode | "is it really fixed", "AI says done", "can I trust this" |

## Multi-Intent Requests

If the user asks for more than one thing, combine modes in this order:

1. Session Brief
2. Acceptance Mode if there is a completion claim
3. Visual Summary if a diagram helps
4. Project Memory if the user wants local records
5. Handoff Pack if the user is moving to a new chat

## Insufficient Information

If the user only provides a vague request, ask for one of:

- The AI coding conversation
- The agent's final summary
- The changed-file list
- The commands or checks that were run
- The project goal or current stage

Do not invent missing context.

## Stage Labels

Use simple stage names:

- Exploration
- First working demo
- Bug fix and stabilization
- Feature expansion
- Pre-release cleanup
- Handoff or maintenance

Mark the stage as "unconfirmed" if the input is too thin.
