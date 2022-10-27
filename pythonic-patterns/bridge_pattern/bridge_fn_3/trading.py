from typing import Callable

GetPricesFunction = Callable[[str], list[int]]
DecideFunction = Callable[[str, GetPricesFunction], bool]
BuySellFunction = Callable[[str, int], None]


def run_bot(
    get_prices: GetPricesFunction,
    should_buy: DecideFunction,
    should_sell: DecideFunction,
    buy: BuySellFunction,
    sell: BuySellFunction,
    symbol: str,
    trade_amount: int,
) -> None:
    if should_buy(symbol, get_prices):
        buy(symbol, trade_amount)
    elif should_sell(symbol, get_prices):
        sell(symbol, trade_amount)
    else:
        print("No action needed.")
