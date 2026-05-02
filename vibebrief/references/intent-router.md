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
| Check a completion claim | Confidence Check / Acceptance Mode | "is it really fixed", "AI says done", "can I trust this" |

## Bare `/vibebrief` Menu

If the user enters only `/vibebrief` and provides no AI coding conversation, logs, terminal output, or natural-language task, show a mode menu.

Do not show the menu when the user gives content or intent after `/vibebrief`; route automatically instead.

Chinese menu:

```text
请选择你想让 VibeBrief 做什么：

1. 本轮开发简报（默认推荐）：我想看懂这轮 AI 到底做了什么
2. 可信度检查：AI 说修好了，我想判断是否真的可靠
3. 新对话交接包：我要换新 chat，希望下一轮能接上
4. 阶段报告：我想判断这轮是否可以作为一个阶段节点
5. 可视化流程图：我想用图看懂流程、风险或修复链路
6. 项目记忆保存：我想把这轮结果整理成可保存的项目资料

如果不确定，直接选 1。
```

English menu:

```text
What would you like VibeBrief to do?

1. Session Brief (recommended default): help me understand what the AI did in this coding session
2. Confidence Check: help me judge whether the AI's "fixed" or "done" claim is actually supported
3. Handoff Pack: prepare a new-chat handoff so the next AI can continue safely
4. Milestone Report: decide whether this session is stable enough to count as a project checkpoint
5. Visual Summary: show the flow, risk, or fix chain with a simple Mermaid diagram
6. Project Memory: turn this session into save-ready project memory

If unsure, choose 1.
```

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
