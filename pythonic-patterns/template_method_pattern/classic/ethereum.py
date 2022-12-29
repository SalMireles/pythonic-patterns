from trading_bot import TradingBot


class EthereumTradingBot(TradingBot):
    def buy(self, amount: int) -> None:
        print(f"Buying {amount/10000000:.7f} Ethereum.")

    def sell(self, amount: int) -> None:
        print(f"Selling {amount/10000000:.7f} Ethereum.")

    def should_buy(self, prices: list[int]) -> bool:
        return prices[-1] > prices[-2]

    def should_sell(self, prices: list[int]) -> bool:
        return prices[-1] < prices[-2]

    def get_price_data(self) -> list[int]:
        return [
            2_381_00,
            2_233_00,
            2_300_00,
            2_342_00,
            2_137_00,
            2_156_00,
            2_103_00,
            2_165_00,
            2_028_00,
            2_004_00,
        ]

    def get_amount(self) -> int:
        return 100000
