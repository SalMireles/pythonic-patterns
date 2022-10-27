import statistics

from trading import GetPricesFunction


def should_buy_avg(
    symbol: str, get_prices: GetPricesFunction, window_size: int = 3
) -> bool:
    prices = get_prices(symbol)
    list_window = prices[-window_size:]
    return prices[-1] < statistics.mean(list_window)


def should_sell_avg(
    symbol: str, get_prices: GetPricesFunction, window_size: int = 3
) -> bool:
    prices = get_prices(symbol)
    list_window = prices[-window_size:]
    return prices[-1] > statistics.mean(list_window)
