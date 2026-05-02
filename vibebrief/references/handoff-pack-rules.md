# Handoff Pack Rules

Handoff Pack prepares a new AI chat or a different agent to continue without losing context.

A Handoff Pack must be understandable by a new AI agent without reading the full prior conversation.

## Required Sections

- Project background
- Current goal
- Current status
- Recent completed work
- Unresolved issues
- Known risks
- Decisions already made
- Traps to avoid
- Next executable prompt

## Prompt Rules

The prompt must be executable by the next AI. It should include:

- The immediate task
- What context to read first
- What not to change
- What evidence to provide before claiming completion
- Whether to avoid feature expansion

## Keep It Compact

The handoff pack should be dense enough to carry context, but short enough to paste into a new chat.

If the user provides too much history, summarize into:

- Background
- Current state
- Open risks
- Next action
