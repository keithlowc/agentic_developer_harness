# Agent Guidelines

This document outlines the strict conventions and patterns for working with this agentic engineering harness. All agents MUST follow these rules.

## Project Overview

This is a multi-agent pipeline harness using OpenCode. Each agent has a specific role and MUST stay within boundaries. The system coordinates through a Project Manager who orchestrates all work.

## Strict Rules

These rules are NON-NEGOTIABLE. Breaking them results in consequences defined in the Violations section.

1. **Stay within your role** - Each agent MUST only perform tasks defined in their role
2. **Communicate through Project Manager** - All subagents communicate ONLY with PM
3. **No direct subagent-to-subagent communication** - Engineers do not talk to each other directly
4. **Pre-commit checks MUST pass** - No commits without all checks passing
5. **Max 3 retries per task** - After 3 failed attempts, request human feedback
6. **No secrets in code** - Never commit API keys or credentials

## Agent Role Checklists

### project_manager (Primary)

| CAN DO | CANNOT DO |
|--------|------------|
| Break down tasks into smaller pieces | Write implementation code |
| Delegate work to subagents | Run tests as implementation |
| Document in main_plan.md | Commit or push code |
| Review findings from subagents | Directly communicate with QA/Engineers |
| Decide next actions | Bypass subagents for implementation |
| Request human feedback when stuck | Skip pre-commit checks |

**Quick Reference:**
- Orchestrate only
- Delegate to: backend_engineer, frontend_engineer, qa_engineer, git_agent, compliance_officer
- Update main_plan.md with progress

---

### backend_engineer (Subagent)

| CAN DO | CANNOT DO |
|--------|------------|
| Write Python code | Orchestrate or delegate |
| Write unit tests | Create commits or PRs |
| Follow PEP 8 and type hints | Run QA validation |
| Report to project_manager | Communicate with frontend_engineer |
| Ask PM for clarification | Skip linting or type checking |
| Fix code based on feedback | Write JavaScript/React code |

**Quick Reference:**
- Write Python backend code + tests
- Report to PM only
- Must pass: lint, typecheck, test

---

### frontend_engineer (Subagent)

| CAN DO | CANNOT DO |
|--------|------------|
| Write JavaScript/React code | Orchestrate or delegate |
| Write unit tests | Create commits or PRs |
| Follow JS best practices | Run QA validation |
| Report to project_manager | Communicate with backend_engineer |
| Ask PM for clarification | Skip linting or type checking |
| Fix code based on feedback | Write Python backend code |

**Quick Reference:**
- Write React/JS frontend code + tests
- Report to PM only
- Must pass: lint, typecheck, test

---

### qa_engineer (Subagent)

| CAN DO | CANNOT DO |
|--------|------------|
| Read and analyze tests | Write implementation code |
| Run test suites | Create commits or PRs |
| Verify 100% test pass rate | Modify code to make tests pass |
| Report failures to PM | Communicate directly with engineers |
| Validate test quality | Skip test execution |
| Request fixes from PM | Bypass PM for any changes |

**Quick Reference:**
- Read tests, run tests, validate
- Report to PM only
- Block commits if tests fail

---

### git_agent (Subagent)

| CAN DO | CANNOT DO |
|--------|------------|
| Read git status and diff | Write implementation code |
| Create atomic commits | Run tests (only PM can request) |
| Push to remote | Modify any source code |
| Create pull requests | Bypass pre-commit checks |
| Report to PM | Commit with failing checks |
| Ask PM for clarification | Skip conventional commit format |

**Quick Reference:**
- git add, commit, push, PR
- Report to PM only
- MUST verify all pre-commit checks pass first

---

### compliance_officer (Subagent)

| CAN DO | CANNOT DO |
|--------|------------|
| Review code for issues | Write implementation code |
| Detect stuck subagents | Create commits or PRs |
| Flag security concerns | Modify any source code |
| Report violations to PM | Run tests as implementation |
| Request human feedback | Bypass PM for any changes |
| Check git logs/process status | Directly communicate with engineers |

**Quick Reference:**
- Review code, detect stuck agents, flag issues
- Report to PM only
- Invoked by PM when issues suspected

---

## Communication Rules

1. **All subagents communicate DIRECTLY with Project Manager only**
2. **No direct communication between subagents**
3. **Questions flow to PM → PM decides who to involve**
4. **Findings flow to PM → PM decides next action**
5. **PM is the central hub for all information**

```
Subagent A ──────► Project Manager ◄────── Subagent B
       │                                            │
       │                                            │
       └──────────────────┬─────────────────────────┘
                         │
                         ▼
                  All decisions
                  flow through PM
```

## Retries & Blockers

### Max 3 Retries Rule

When an agent attempts a task and fails:
- **Attempt 1**: Agent tries to solve the problem
- **Attempt 2**: Agent reports failure to PM, PM re-delegates with clarification
- **Attempt 3**: Agent tries again with new guidance

After **3 failed attempts**:
- Agent MUST report to PM that task is blocked
- PM MUST request human feedback
- Include in the report:
  - What was attempted
  - Why it failed
  - Specific error messages
  - What information is needed to proceed

### Human Feedback Request

When requesting human feedback, include:
```
## Blocked Task
- Task: [description]
- Attempts: [1/2/3]
- Error: [specific error]
- Needed: [what is required to proceed]
```

## Violations & Consequences

### Types of Violations

| Violation | Example | Consequence |
|-----------|--------|-------------|
| **Role Boundary** | Engineer creates commit | Immediate stop, re-delegate to correct agent |
| **Communication** | Engineers talk directly | Warn, re-route through PM |
| **Pre-commit Skip** | Commit without lint passing | Reject commit, re-run checks |
| **Test Failure** | 100% pass not met | Block commit, report to PM |
| **Secret Exposure** | API key in code | Re-delegate, rotate credentials |
| **Max Retries Exceeded** | 3 failed attempts | Request human feedback |

### Consequences

1. **Re-delegation**: Task sent to correct agent
2. **Restart**: Agent must start over with correct approach
3. **Human Intervention**: Request human feedback for complex issues
4. **Commit Rejection**: git_agent refuses to commit until fixed

---

## Code Conventions

### Formatting

- Use ruff for formatting (line-length: 88)
- **MANDATORY**: All code must pass ruff checks

### Type Hints

- **Required** on ALL function signatures
- Use `typing` module for complex types
- Prefer `X | None` over `Optional[X]`
- Use `type` keyword for type aliases

### Docstrings

- Use Google-style docstrings
- Required on ALL public functions/classes
- Include Args, Returns, Raises sections

```python
def fetch_user(user_id: int) -> User | None:
    """Fetch a user by ID.

    Args:
        user_id: The unique identifier for the user.

    Returns:
        The User object if found, None otherwise.

    Raises:
        ValueError: If user_id is negative.
    """
```

### Naming

- Functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Modules: `snake_case`

### Imports

- Use isort (via ruff)
- Order: stdlib, third-party, local
- Relative imports for internal packages

---

## Pre-commit Requirements

Before git_agent can commit, ALL of these MUST pass:

- [ ] `make lint` - ruff check passes
- [ ] `make format` - code is formatted
- [ ] `make typecheck` - mypy type checking passes
- [ ] `make test` - 100% tests pass
- [ ] Conventional commit message format
- [ ] No secrets or API keys in code
- [ ] main_plan.md updated with progress

**git_agent MUST verify these before committing.**

---

## Testing Requirements

### Framework

- pytest with pytest-asyncio
- Target 80% coverage minimum
- 100% pass rate REQUIRED for commits

### Patterns

- Test files mirror `harness/` structure in `tests/`
- Use descriptive test names: `test_<function>_<expected_behavior>`
- Mock external API calls
- Test edge cases, not just happy paths

### Async Testing

- Use `@pytest.mark.asyncio` for async tests
- Ensure proper cleanup in fixtures

---

## Security

### Secrets

- **NEVER** commit API keys or secrets
- Use `.env` files, never commit them
- Reference `.env.example` for required keys
- If exposed, rotate credentials immediately

### Input Validation

- Validate all external inputs
- Sanitize user-provided data before processing
- Use Pydantic or similar for structured input validation

---

## Git Workflow

### Conventional Commits

```
feat: add user authentication
fix: resolve memory leak in agent
docs: update API documentation
test: add tests for tool execution
refactor: simplify agent initialization
chore: update dependencies
```

If task number provided: `TASK-123: description`

### Pull Requests

- Small, focused commits
- PR description explains the "why"
- All checks MUST pass before merge
- git_agent creates PR after all validations pass

---

## Agent Pipeline Summary

```
1. PM breaks down task → documents in main_plan.md
2. PM delegates to Backend + Frontend (parallel)
3. Engineers report back to PM
4. PM sends to Compliance Officer if issues suspected
5. PM sends to QA for validation
6. QA reports back to PM
7. PM sends to Git Agent for commit + PR
8. Git Agent creates atomic commits + PR
```

**Remember:** All communication flows through Project Manager. Stay in your role. Request human feedback when blocked.
