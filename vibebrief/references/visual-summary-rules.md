# Visual Summary Rules

Visual Summary uses Mermaid to make a coding session or stage understandable.

## Allowed Diagram Types

Use at least one:

- Task flowchart
- Stage roadmap
- Bug-fix chain
- Risk status map
- Human-AI collaboration swimlane

## Style Rules

- Keep labels short and plain.
- Avoid deep engineering internals unless the user asks.
- Show verification state when relevant.
- After the diagram, explain it in simple language.
- If the diagram would expose private names, generalize them.

## Example Patterns

### Task Flow

```mermaid
flowchart LR
    A[User goal] --> B[AI changed files]
    B --> C[Claimed result]
    C --> D{Verified?}
    D -->|No| E[Ask for evidence]
    D -->|Yes| F[Record progress]
```

### Risk Map

```mermaid
flowchart TD
    A[Current stage] --> B[Verified]
    A --> C[Unverified]
    A --> D[Risk]
    C --> E[Run minimum check]
    D --> F[Narrow next task]
```

### Collaboration Swimlane

```mermaid
flowchart LR
    U[User: defines goal] --> AI[AI: changes code]
    AI --> V[VibeBrief: explains and records]
    V --> U2[User: decides next step]
```
