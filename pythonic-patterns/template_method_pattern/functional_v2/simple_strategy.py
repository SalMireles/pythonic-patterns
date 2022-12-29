class SimpleStrategy:
    def should_buy(self, prices: list[int]) -> bool:
        return prices[-1] > prices[-2]

    def should_sell(self, prices: list[int]) -> bool:
        return prices[-1] < prices[-2]
