import statistics
from dataclasses import dataclass

from exchange import Exchange


@dataclass
class AverageTradingBot:
    exchange: Exchange
    window_size: int = 3

    def should_buy(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        list_window = prices[-self.window_size :]
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        list_window = prices[-self.window_size :]
        return prices[-1] > statistics.mean(list_window)
