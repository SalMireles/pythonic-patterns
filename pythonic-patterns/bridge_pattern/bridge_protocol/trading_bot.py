from typing import Protocol


class TradingBot(Protocol):
    def should_buy(self, symbol: str) -> bool:
        pass

    def should_sell(self, symbol: str) -> bool:
        pass
