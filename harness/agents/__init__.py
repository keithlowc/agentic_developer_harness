"""Base agent implementation."""

from typing import Any
from unittest.mock import MagicMock


class Agent:
    """Base agent class."""

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        self.config = config or {}

    async def run(self, prompt: str) -> Any:
        """Run the agent with a prompt.

        Args:
            prompt: The input prompt.

        Returns:
            Agent response.

        Raises:
            ValueError: If prompt is empty.
        """
        if not prompt:
            raise ValueError("Prompt cannot be empty")
        return {"response": "stub response"}


class LLMClient:
    """Mock LLM client for testing."""

    def generate(self, prompt: str) -> Any:
        """Generate a response."""
        return MagicMock(content="Mock response")
