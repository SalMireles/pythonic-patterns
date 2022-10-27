from trading import GetPricesFunction


def should_buy_minmax(
    symbol: str, get_prices: GetPricesFunction, min_price: int = 32_000_00
) -> bool:
    prices = get_prices(symbol)
    return prices[-1] < min_price


def should_sell_minmax(
    symbol: str, get_prices: GetPricesFunction, max_price: int = 33_000_00
) -> bool:
    prices = get_prices(symbol)
    return prices[-1] > max_price
