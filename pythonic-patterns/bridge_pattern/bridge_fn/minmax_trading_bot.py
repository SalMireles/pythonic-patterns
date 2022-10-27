from exchange import Exchange


def should_buy_minmax(
    symbol: str, exchange: Exchange, min_price: int = 32_000_00
) -> bool:
    prices = exchange.get_prices(symbol)
    return prices[-1] < min_price


def should_sell_minmax(
    symbol: str, exchange: Exchange, max_price: int = 33_000_00
) -> bool:
    prices = exchange.get_prices(symbol)
    return prices[-1] > max_price
