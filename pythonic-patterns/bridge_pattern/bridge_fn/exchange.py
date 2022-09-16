from typing import Protocol


class Exchange(Protocol):
    def get_prices(self, symbol: str) -> list[int]:
        """Get the prices of the given symbol."""

    def buy(self, symbol: str, amount: int) -> None:
        """Buy the given amount of the given symbol."""

    def sell(self, symbol: str, amount: int) -> None:
        """Sell the given amount of the given symbol."""
