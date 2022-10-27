import statistics

from exchange import Exchange


def should_buy_avg(symbol: str, exchange: Exchange, window_size: int = 3) -> bool:
    prices = exchange.get_prices(symbol)
    list_window = prices[-window_size:]
    return prices[-1] < statistics.mean(list_window)


def should_sell_avg(symbol: str, exchange: Exchange, window_size: int = 3) -> bool:
    prices = exchange.get_prices(symbol)
    list_window = prices[-window_size:]
    return prices[-1] > statistics.mean(list_window)
