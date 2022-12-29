from abc import ABC, abstractmethod


class TradingBot(ABC):
    @abstractmethod
    def buy(self, amount: int) -> None:
        """Buy the given amount."""

    @abstractmethod
    def sell(self, amount: int) -> None:
        """Sell the given amount."""

    @abstractmethod
    def should_buy(self, prices: list[int]) -> bool:
        """Should the bot buy?"""

    @abstractmethod
    def should_sell(self, prices: list[int]) -> bool:
        """Should the bot sell?"""

    @abstractmethod
    def get_price_data(self) -> list[int]:
        """Get the price data."""

    @abstractmethod
    def get_amount(self) -> int:
        """Get the amount to trade."""

    def trade(self) -> None:
        prices = self.get_price_data()
        amount = self.get_amount()

        if self.should_buy(prices):
            self.buy(amount)
        if self.should_sell(prices):
            self.sell(amount)
