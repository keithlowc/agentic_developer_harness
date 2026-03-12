.PHONY: install-dev lint typecheck test format clean

install-dev:
	@echo "Installing development dependencies..."
	pre-commit install
	pip install -e ".[dev]"

lint:
	@echo "Running ruff..."
	ruff check . && ruff format --check .

typecheck:
	@echo "Running mypy..."
	mypy harness/

test:
	@echo "Running tests..."
	pytest

test-cov:
	@echo "Running tests with coverage..."
	pytest --cov=harness --cov-report=term-missing --cov-report=html

format:
	@echo "Formatting code..."
	ruff format . && ruff check --fix .

clean:
	@echo "Cleaning up..."
	rm -rf .pytest_cache/ .mypy_cache/ .ruff_cache/
	rm -rf htmlcov/ .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
