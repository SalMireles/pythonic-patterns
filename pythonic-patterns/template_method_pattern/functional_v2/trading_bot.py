from typing import Protocol


class TradingEngine(Protocol):
    def buy(self, amount: int) -> None:
        """Buy some crypto currency."""

    def sell(self, amount: int) -> None:
        """Sell some crypto currency."""

    def get_price_data(self) -> list[int]:
        """Get the price data."""

    def get_amount(self) -> int:
        """Get the trading amount."""


class TradingStrategy(Protocol):
    def should_buy(self, prices: list[int]) -> bool:
        """Should we buy?"""

    def should_sell(self, prices: list[int]) -> bool:
        """Should we sell?"""


def trade(engine: TradingEngine, strategy: TradingStrategy) -> None:
    prices = engine.get_price_data()
    amount = engine.get_amount()

    if strategy.should_buy(prices):
        engine.buy(amount)
    if strategy.should_sell(prices):
        engine.sell(amount)
