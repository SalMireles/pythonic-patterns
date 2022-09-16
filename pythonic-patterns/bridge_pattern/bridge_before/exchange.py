from abc import ABC, abstractmethod


class Exchange(ABC):
    @abstractmethod
    def get_prices(self, symbol: str) -> list[int]:
        """Get the prices of the given symbol."""

    @abstractmethod
    def buy(self, symbol: str, amount: int) -> None:
        """Buy the given amount of the given symbol."""

    @abstractmethod
    def sell(self, symbol: str, amount: int) -> None:
        """Sell the given amount of the given symbol."""
