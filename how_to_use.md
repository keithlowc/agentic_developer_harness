# How to Use This Agent Harness

This guide explains how to use the OpenCode-based agent harness for coordinated software development.

## Prerequisites

1. **OpenCode CLI** - Install from [opencode.ai](https://opencode.ai)
2. **API Keys** - Set up your preferred LLM provider:
   - OpenAI (`OPENAI_API_KEY`)
   - Anthropic (`ANTHROPIC_API_KEY`)
   - Or configure another provider in `opencode.json`

## Quick Start

1. **Configure the model** (optional):

   Edit `opencode.json` to choose your preferred model:

   ```json
   {
     "model": "opencode/minimax-m2.5-free"
   }
   ```

2. **Install dependencies**:

   ```bash
   make install-dev
   ```

3. **Run OpenCode**:

   ```bash
   opencode
   ```

   This starts the CLI with the `project_manager` as the default agent.

## How It Works

### 1. Start a Task

When you run `opencode`, you're interacting with the **project_manager** agent. Describe what you want to build:

```
I want to build a REST API for managing tasks
```

### 2. Project Manager Plans

The project_manager will:
- Break down your task into smaller pieces
- Document the plan in `main_plan.md`
- Delegate work to specialized agents

### 3. Agents Work in Parallel

Depending on the task, the project_manager may delegate to:

| Agent | Handles |
|-------|---------|
| `backend_engineer` | Python backend code |
| `frontend_engineer` | React/JavaScript frontend |
| `qa_engineer` | Test validation |
| `git_agent` | Version control & PRs |

### 4. Review & Iterate

- Engineers report back to project_manager
- QA validates tests pass
- Project_manager decides next steps

## Example Workflow

```
You: I need a user authentication system

Project Manager: [creates plan in main_plan.md]
- Delegate backend: auth endpoints + tests
- Delegate frontend: login/signup forms
- QA validates
- Git agent commits + PR

> Starts delegating to backend_engineer and frontend_engineer
```

## Configuration

### Changing the Model

Edit the `model` field in `opencode.json`:

```json
{
  "model": "anthropic/claude-3-sonnet"
}
```

### Adding Custom Agents

Define new agents in `opencode.json` under the `agent` section:

```json
"agent": {
  "your_agent": {
    "description": "Your custom agent",
    "mode": "subagent",
    "prompt": "Your agent instructions...",
    "tools": {
      "read": true,
      "write": true
    }
  }
}
```

## File Structure

```
.
├── opencode.json       # Agent configuration
├── pyproject.toml     # Python project settings
├── .pre-commit-config.yaml
├── Makefile           # Development commands
├── main_plan.md       # Task planning (auto-generated)
├── README.md          # Project overview
└── AGENTS.md          # Agent conventions
```

## Troubleshooting

### Agent is stuck

If an agent is taking too long or stuck in a loop:
1. Press `Ctrl+C` to interrupt
2. The project_manager will reassess and re-delegate

### Need to reset

To start fresh:
1. Clear `main_plan.md`
2. Run `opencode` again with your new request

### Check agent logs

Review `main_plan.md` for the current task breakdown and status.

## Best Practices

1. **Be specific** - Clear requirements produce better results
2. **Incremental changes** - Small tasks work better than large ones
3. **Review plans** - Check `main_plan.md` before agents proceed
4. **Iterate** - It's okay to refine requirements mid-task
