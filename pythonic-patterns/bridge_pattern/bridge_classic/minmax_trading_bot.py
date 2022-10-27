from dataclasses import dataclass

from trading_bot import TradingBot


@dataclass
class MinMaxTradingBot(TradingBot):
    min_price: int = 32_000_00
    max_price: int = 33_000_00

    def should_buy(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        return prices[-1] < self.min_price

    def should_sell(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        return prices[-1] > self.max_price
