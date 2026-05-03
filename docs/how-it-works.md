# How It Works

VibeBrief is a prompt-and-reference skill. It helps an AI assistant produce clearer notes from AI coding conversations.

## 1. Route The Intent

VibeBrief first decides which mode fits the user's request:

- Session Brief
- Milestone Report
- Handoff Pack
- Visual Summary
- Project Memory
- Confidence Check

The user can use natural language. Commands are optional.

## 2. Translate Technical Work

The skill translates technical changes into plain language.

## 3. Keep Uncertainty Visible

VibeBrief must not invent proof. If something is unclear, it should say so.

## 4. Preserve Continuity

When the user asks for memory or handoff, VibeBrief creates compact notes for future context.

## 5. Use Scripts Only For Lightweight Help

The scripts do not run product tests or make commits. They only:

- Collect basic local context
- Write memory files
- Update a lightweight index
- Check the repository structure before publishing
