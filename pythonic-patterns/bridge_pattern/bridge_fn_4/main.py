from functools import partial

from avg_trading_bot import should_buy_avg, should_sell_avg
from coinbase import buy, get_prices, sell
from trading import run_bot

SYMBOL = "BTC/USD"
TRADE_AMOUNT = 10


def main() -> None:
    should_buy = partial(should_buy_avg, symbol=SYMBOL, get_prices=get_prices)
    should_sell = partial(should_sell_avg, symbol=SYMBOL, get_prices=get_prices)
    buy_fn = partial(buy, symbol=SYMBOL, amount=TRADE_AMOUNT)
    sell_fn = partial(sell, symbol=SYMBOL, amount=TRADE_AMOUNT)
    run_bot(should_buy, should_sell, buy_fn, sell_fn)


if __name__ == "__main__":
    main()
