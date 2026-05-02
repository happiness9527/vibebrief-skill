# How It Works

VibeBrief is a prompt-and-reference skill. It teaches an AI assistant how to turn coding conversations into project memory.

## 1. Route The Intent

VibeBrief first decides which mode fits the user's request:

- Session Brief
- Milestone Report
- Handoff Pack
- Visual Summary
- Project Memory
- Acceptance Mode

The user can use natural language. Commands are optional.

## 2. Translate Technical Work

The skill translates technical changes into plain-language project meaning.

Instead of only saying `controller.py changed`, it should explain what that controller likely means for the product flow.

## 3. Separate Claims From Evidence

VibeBrief must not invent proof. It separates:

- Changed
- Verified
- Unverified
- Risky
- Safe to continue
- Not recommended to continue

## 4. Preserve Continuity

When the user asks for memory or handoff, VibeBrief creates content that can be reused in the next AI coding session.

## 5. Use Scripts Only For Lightweight Help

The scripts do not run product tests or make commits. They only:

- Collect basic local context
- Write memory files
- Update a JSON index
- Check the repository structure before publishing
