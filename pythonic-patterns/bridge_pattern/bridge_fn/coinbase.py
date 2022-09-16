PRICE_DATA = {
    "BTC/USD": [
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
    ],
    "ETH/USD": [
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
    ],
}


class Coinbase:
    def get_prices(self, symbol: str) -> list[int]:
        return PRICE_DATA[symbol]

    def buy(self, symbol: str, amount: int) -> None:
        print(f"[Coinbase] Buying amount {amount} in market {symbol}.")

    def sell(self, symbol: str, amount: int) -> None:
        print(f"[Coinbase] Selling amount {amount} in market {symbol}.")
