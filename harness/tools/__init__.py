"""Tool definition."""

from typing import Any, Callable


class Tool:
    """Base tool class."""

    def __init__(
        self,
        name: str,
        description: str,
        execute: Callable[[], Any] | None = None,
    ) -> None:
        self.name = name
        self.description = description
        self._execute = execute

    def execute(self) -> Any:
        """Execute the tool."""
        if self._execute is None:
            return {"status": "not implemented"}
        return self._execute()
