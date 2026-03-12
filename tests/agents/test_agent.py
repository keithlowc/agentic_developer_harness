"""Tests for agent module."""

import pytest
from unittest.mock import MagicMock, patch


class TestAgent:
    """Test suite for Agent class."""

    def test_agent_initialization(self) -> None:
        """Test that agent initializes with default settings."""
        from harness.agents import Agent

        agent = Agent()
        assert agent is not None

    def test_agent_accepts_custom_config(self) -> None:
        """Test that agent accepts custom configuration."""
        from harness.agents import Agent

        config = {"model": "gpt-4", "temperature": 0.5}
        agent = Agent(config=config)
        assert agent.config == config

    @pytest.mark.asyncio
    async def test_agent_run_returns_response(self, mock_llm_response: MagicMock) -> None:
        """Test that agent.run returns a valid response."""
        from harness.agents import Agent

        with patch("harness.agents.LLMClient") as mock_client:
            mock_client.return_value.generate.return_value = mock_llm_response
            agent = Agent()
            result = await agent.run("test prompt")
            assert result is not None

    @pytest.mark.asyncio
    async def test_agent_handles_empty_prompt(self) -> None:
        """Test that agent handles empty prompt gracefully."""
        from harness.agents import Agent

        agent = Agent()
        with pytest.raises(ValueError):
            await agent.run("")


class TestTool:
    """Test suite for Tool class."""

    def test_tool_has_name(self) -> None:
        """Test that tool has a name attribute."""
        from harness.tools import Tool

        tool = Tool(name="test_tool", description="A test tool")
        assert tool.name == "test_tool"

    def test_tool_execution(self, mock_tool_result: dict) -> None:
        """Test that tool executes and returns result."""
        from harness.tools import Tool

        def execute_func() -> dict:
            return mock_tool_result

        tool = Tool(name="test", description="test", execute=execute_func)
        result = tool.execute()
        assert result == mock_tool_result
