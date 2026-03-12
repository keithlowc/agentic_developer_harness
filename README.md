# Agent Harness

A boilerplate for developers building agentic engineering systems in Python.

## Quick Start

```bash
# Install dependencies
make install-dev

# Run tests
make test

# Format code
make format
```

## Project Structure

```
harness/           # Main package
  agents/          # Agent implementations
  tools/           # Tool definitions
  utils/           # Shared utilities
tests/             # Test suite
```

## Available Commands

| Command | Description |
|---------|-------------|
| `make install-dev` | Install dev dependencies and pre-commit hooks |
| `make lint` | Run ruff linting and format check |
| `make typecheck` | Run mypy type checking |
| `make test` | Run pytest |
| `make test-cov` | Run tests with coverage report |
| `make format` | Format code with ruff |
| `make clean` | Clean up cache files |
