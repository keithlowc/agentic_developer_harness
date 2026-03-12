"""Shared test fixtures."""

import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_llm_response() -> MagicMock:
    """Mock LLM response for testing."""
    mock = MagicMock()
    mock.content = "Test response"
    mock.model = "gpt-4"
    return mock


@pytest.fixture
def mock_tool_result() -> dict[str, object]:
    """Mock tool execution result."""
    return {"status": "success", "data": {"result": "tool output"}}
