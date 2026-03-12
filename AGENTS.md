# Agent Guidelines

This document outlines the conventions and patterns for contributing to this project.

## Project Overview

This is a Python agentic engineering harness providing foundational patterns for building AI agents with tool-calling capabilities.

## Tech Stack

- Python 3.10+
- pytest (testing)
- ruff (linting & formatting)
- mypy (type checking)
- pre-commit (git hooks)

## Code Conventions

### Formatting

- Use ruff for formatting (line-length: 88)
- Run `make format` before committing

### Type Hints

- **Required** on all function signatures
- Use `typing` module for complex types
- Prefer `X | None` over `Optional[X]`
- Use `type` keyword for type aliases

### Docstrings

- Use Google-style docstrings
- Required on all public functions/classes
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

## Project Structure

```
harness/
  __init__.py
  agents/           # Agent implementations
    __init__.py
  tools/            # Tool definitions
    __init__.py
  utils/            # Shared utilities
    __init__.py
tests/
  agents/
  tools/
  utils/
```

## Testing Requirements

### Framework

- pytest with pytest-asyncio
- Target 80% coverage minimum

### Patterns

- Test files mirror `harness/` structure in `tests/`
- Use descriptive test names: `test_<function>_<expected_behavior>`
- Mock external API calls
- Test edge cases, not just happy paths

```python
class TestAgent:
    def test_agent_returns_valid_response(self, mock_llm):
        agent = Agent()
        result = agent.run("test prompt")
        assert isinstance(result, Response)
```

### Async Testing

- Use `@pytest.mark.asyncio` for async tests
- Ensure proper cleanup in fixtures

## Security

### Secrets

- **NEVER** commit API keys or secrets
- Use `.env` files, never commit them
- Reference `.env.example` for required keys

### Input Validation

- Validate all external inputs
- Sanitize user-provided data before processing
- Use Pydantic or similar for structured input validation

## Git Workflow

### Commits

Use conventional commits:

```
feat: add user authentication
fix: resolve memory leak in agent
docs: update API documentation
test: add tests for tool execution
refactor: simplify agent initialization
```

### Pre-commit

Pre-commit hooks run automatically. To manually run:

```bash
make lint
make typecheck
make test
```

### Pull Requests

- Small, focused commits
- PR description explains the "why"
- All checks must pass before merge

## Common Commands

```bash
make install-dev   # Install dependencies + pre-commit hooks
make lint          # Check code style
make typecheck     # Type check
make test          # Run tests
make format        # Auto-format code
make clean         # Remove cache files
```
