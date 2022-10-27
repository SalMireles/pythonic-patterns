from exchange import Exchange

PRICE_DATA = {
    "BTC/USD": [
        35_838_00,
        34_064_00,
        33_879_00,
        34_219_00,
        32_912_00,
        33_929_00,
        33_377_00,
        34_448_00,
        32_911_00,
        33_009_00,
    ],
    "ETH/USD": [
        2_378_00,
        2_234_00,
        2_302_00,
        2_347_00,
        2_235_00,
        2_152_00,
        2_112_00,
        2_168_00,
        2_035_00,
        2_009_00,
    ],
}


class Binance(Exchange):
    def get_prices(self, symbol: str) -> list[int]:
        return PRICE_DATA[symbol]

    def buy(self, symbol: str, amount: int) -> None:
        print(f"[Binance] Buying amount {amount} in market {symbol}.")

    def sell(self, symbol: str, amount: int) -> None:
        print(f"[Binance] Selling amount {amount} in market {symbol}.")
