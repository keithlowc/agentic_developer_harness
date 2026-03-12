.PHONY: install-dev lint typecheck test format clean

install-dev:
	@echo "Installing development dependencies..."
	pre-commit install
	pip install -e ".[dev]"
