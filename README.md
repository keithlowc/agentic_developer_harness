# Agent Harness

A boilerplate for building AI agent pipelines with OpenCode. This harness provides a multi-agent system for coordinated software development.

## Overview

This project provides a pre-configured OpenCode pipeline with specialized agents that work together to:
- Break down tasks and plan development
- Implement backend and frontend code in parallel
- Write and validate tests
- Create atomic commits and pull requests

## Agents

| Agent | Type | Description |
|-------|------|-------------|
| `project_manager` | Primary | Orchestrates tasks, delegates work, documents in `main_plan.md` |
| `backend_engineer` | Subagent | Python backend development, writes code + tests |
| `frontend_engineer` | Subagent | React/JavaScript frontend development, writes code + tests |
| `qa_engineer` | Subagent | Validates tests, ensures 100% pass rate |
| `git_agent` | Subagent | Creates atomic commits and opens pull requests |

## Pipeline Flow

1. **Project Manager** breaks down tasks and documents in `main_plan.md`
2. **Project Manager** delegates to Backend + Frontend (parallel when possible)
3. Both engineers work and report back to **Project Manager**
4. **Project Manager** sends to **QA Engineer** for validation
5. **QA Engineer** runs tests and reports back to **Project Manager**
6. **Project Manager** sends to **Git Agent** for commit and PR creation

All subagents communicate directly with Project Manager.

## Quick Start

```bash
# Install dependencies
make install-dev
```

## Configuration

### Model

The default model is set in `opencode.json`. Change `model` to your preferred provider.

## Available Commands

| Command | Description |
|---------|-------------|
| `make install-dev` | Install dev dependencies and pre-commit hooks |

## Files

| File | Description |
|------|-------------|
| `opencode.json` | OpenCode agent configuration |
| `pyproject.toml` | Python project configuration |
| `.pre-commit-config.yaml` | Pre-commit hook configuration |
| `.gitignore` | Git ignore patterns |
| `AGENTS.md` | Agent guidelines and conventions |
| `main_plan.md` | Task planning template |
| `Makefile` | Common development commands |
