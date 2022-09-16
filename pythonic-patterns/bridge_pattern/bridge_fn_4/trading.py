from typing import Callable

GetPricesFunction = Callable[[str], list[int]]
DecideFunction = Callable[[str, GetPricesFunction], bool]
BuySellFunction = Callable[[str, int], None]


def run_bot(
    should_buy: Callable[[], bool],
    should_sell: Callable[[], bool],
    buy: Callable[[], None],
    sell: Callable[[], None],
) -> None:
    if should_buy():
        buy()
    elif should_sell():
        sell()
    else:
        print("No action needed.")
