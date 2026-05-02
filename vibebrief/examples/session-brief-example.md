# Session Brief Example

## Input

Fictional project: DemoDesk.

```text
I fixed the workspace window sync issue by changing demo_web_app.py and controller.py.
The app should now open the correct course window when /workspace starts.
```

## VibeBrief Output

**Current stage:** Bug fix and stabilization.

**Session goal:** Fix the workspace window sync problem.

**What the AI actually did:**

- It says it changed the web app entry file.
- It says it changed the controller that coordinates workspace windows.

**Why this matters for the project:**

- If correct, users should land in the intended course workspace instead of a mismatched or stale window.
- This improves confidence in the core demo flow.

**Key files or modules:**

- `demo_web_app.py`: likely controls how the demo web app starts.
- `controller.py`: likely coordinates the workspace state and window behavior.

**Verified:**

- Unconfirmed. The input does not include command output, test output, or a screenshot.

**Unverified:**

- Whether `/workspace` really opens the correct window.
- Whether the fix works after a fresh restart.

**Current risk:**

- The AI used "should", so this is a claim, not proof.

**Next step:**

- Ask the AI to run the smallest startup check and show the result.

**Prompt for the next AI:**

```text
Please run the smallest check for the DemoDesk workspace window sync fix.
Start `/workspace`, show the exact command or manual action, and provide the result.
Do not expand features until the startup behavior is verified.
```
