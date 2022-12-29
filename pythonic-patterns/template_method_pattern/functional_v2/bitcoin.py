class BitcoinTradingEngine:
    def buy(self, amount: int) -> None:
        print(f"Buying {amount} BTC satoshi.")

    def sell(self, amount: int) -> None:
        print(f"Selling {amount} BTC satoshi.")

    def get_price_data(self) -> list[int]:
        return [
            35_842_00,
            34_069_00,
            33_871_00,
            34_209_00,
            32_917_00,
            33_931_00,
            33_370_00,
            34_445_00,
            32_901_00,
            33_013_00,
        ]

    def get_amount(self) -> int:
        return 10
