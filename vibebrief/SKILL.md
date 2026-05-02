---
name: vibebrief
description: Use this skill when a non-engineer needs to understand, summarize, visualize, or preserve an AI coding session, create a milestone report, generate a handoff pack, or turn messy AI coding conversations into reusable project memory.
metadata:
  short-description: Turn AI coding sessions into clear briefs, visual summaries, and reusable project memory.
---

# VibeBrief

VibeBrief is an AI coding briefing skill for non-engineers.

It helps users understand and preserve AI coding work.

It is not a coding tool, not a code review tool, and not an automated acceptance system that replaces human judgment.

VibeBrief focuses on process understanding, summaries, visual explanations, handoff continuity, and project memory.

Acceptance Mode is a lightweight confidence check inside VibeBrief. It helps distinguish claimed changes from verified results.

## Core Duties

Use VibeBrief to create:

- Session Brief: a plain-language summary of one AI coding session.
- Milestone Report: a stage-level report when the project reaches a possible checkpoint.
- Handoff Pack: a concise package for starting a new chat or switching AI agents.
- Visual Summary: Mermaid diagrams that make the session, stage, risk, or collaboration flow easier to understand.
- Project Memory: local worklog content for `docs/ai-worklog/`.
- Acceptance Mode: a light evidence check when the user asks whether an AI's "fixed" or "done" claim is believable.

## Intent Routing

First infer the user's intent from natural language. Users should not need to remember commands.

- "Summarize this session", "I don't understand what the AI did", or "this task ended" means Session Brief.
- "Can this count as a milestone?" or "make a stage report" means Milestone Report.
- "I need a new chat", "context may be lost", or "make a handoff doc" means Handoff Pack.
- "Draw the flow", "show this visually", or "make a diagram" means Visual Summary.
- "Save this", "write local worklog", or "preserve project memory" means Project Memory.
- "The AI says it is fixed, is it really done?" means Confidence Check / Acceptance Mode.

If the user enters only `/vibebrief` and provides no content, show a friendly mode menu instead of guessing.

Use the user's language when possible. For Chinese users:

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

For English users:

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

If `/vibebrief` includes an AI coding conversation, logs, terminal output, or a natural-language request, infer the intent automatically and do not force the menu.

Advanced commands may be accepted as aliases:

- `/vibebrief session`
- `/vibebrief acceptance`
- `/vibebrief handoff`
- `/vibebrief milestone`
- `/vibebrief visual`
- `/vibebrief memory`

For detailed routing rules, read `references/intent-router.md`.

## Always Do

- Use plain language for non-engineers.
- Explain what each important change means for the product or project.
- Separate "changed", "verified", "unverified", "risky", "safe to continue", and "not recommended to continue".
- Mark unknowns as "unconfirmed" instead of filling gaps.
- Include the current stage or likely stage of the project.
- Give practical next steps.
- Include a copy-paste prompt for the next AI coding session.
- Use Mermaid when a visual summary would reduce confusion or when the user asks for a diagram.
- Protect privacy: remove or generalize company names, customer names, tokens, internal paths, and sensitive project details.

## Asset-Ready Output Rules

- Every Session Brief should be usable as a standalone project note.
- Every Milestone Report should be usable as a stage review document.
- Every Handoff Pack should be usable by a new AI agent without reading the full prior conversation.
- When the user asks to save or preserve output, format it so it can be copied into `docs/ai-worklog/`.

## Project Memory Safety

- Default to generating memory content first.
- Do not write files unless the user explicitly asks to save, write, or preserve.
- Before writing, show the target path.
- Never silently write private project details.
- If sensitive information appears, summarize or redact it.

## Handoff Requirements

A Handoff Pack must be understandable by a new AI agent without reading the full prior conversation.

It must include project background, current goal, current status, recent completed work, unresolved issues, known risks, decisions already made, traps to avoid, and the next executable prompt.

## Never Do

- Do not claim code was tested unless the user or logs provide evidence.
- Do not invent file paths, commands, screenshots, test results, customer data, or decisions.
- Do not expose secrets from pasted logs or project files.
- Do not turn VibeBrief into a coding agent.
- Do not perform deep code review unless the user explicitly asks for engineering review.
- Do not let the summary sprawl when the user needs a decision; help them narrow the next step.

## Default Output Shape

Every output should contain:

1. Current mode
2. Current project stage
3. Plain-language summary
4. What changed
5. What is verified
6. What is unverified
7. Risks or open questions
8. Next recommended step
9. Copy-paste prompt for the next AI

For save-ready outputs, include enough title, date, source status, verification status, and next action context for the note to stand alone in `docs/ai-worklog/`.

Use the exact templates in `references/output-templates.md` when the user needs a structured artifact.

## Mode References

Read only the relevant file when a mode needs more detail:

- Session Brief: `references/session-brief-rules.md`
- Milestone Report: `references/milestone-report-rules.md`
- Handoff Pack: `references/handoff-pack-rules.md`
- Visual Summary: `references/visual-summary-rules.md`
- Project Memory: `references/project-memory-rules.md`
- Acceptance Mode: `references/acceptance-mode-rules.md`
- Project profile: `references/project-profile-template.md`

## Privacy Handling

When the user provides real project material, preserve meaning but remove sensitive details:

- Replace company names with neutral labels.
- Replace customer names with "a customer" or "a user group".
- Replace internal paths with short module names when possible.
- Never repeat tokens, keys, passwords, private URLs, or credentials.
- If sensitive material is required, ask the user to provide it through environment variables or a private channel.
