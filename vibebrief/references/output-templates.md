# Output Templates

Use this file as lightweight guidance. Do not treat it as a rigid report generator.

## Bare `/vibebrief` Menu

Use this only when the user enters `/vibebrief` without content or a clear task.

Chinese:

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

English:

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

## Session Brief Guidance

A session brief should usually cover:

- Goal
- Actual work
- Confirmed vs unconfirmed status
- Risks
- Next step

Keep it short unless the user asks for a fuller record.

## Milestone Report Guidance

A milestone report should help the user decide whether a stage is stable enough to preserve. Keep the focus on the stage goal, current capability, known uncertainty, and next boundary.

## Handoff Pack Guidance

A handoff pack should be understandable by a new AI agent without the full prior conversation. Keep it compact enough to paste into a new chat.

## Confidence Check Guidance

A confidence check should separate the AI's claim from available evidence and name the smallest reasonable verification step. Do not claim something was tested unless evidence is present.

## Visual Summary Guidance

Use Mermaid only when it makes the situation easier to understand. Keep labels short and explain the diagram in plain language.
