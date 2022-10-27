""" Implementation of trading bot with protocols instead of ABC.

Notice that the exchange connection is happening at the subclass level (duplication),
but we completely got rid of inheritance.

Interesting: Also had to switch to a dataclass with arg of type Exchange.
"""
from avg_trading_bot import AverageTradingBot
from coinbase import Coinbase


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10

    # create the exchange
    exchange = Coinbase()

    # create the trading bot
    trading_bot = AverageTradingBot(exchange)

    should_buy = trading_bot.should_buy(symbol)
    should_sell = trading_bot.should_sell(symbol)
    if should_buy:
        exchange.buy(symbol, trade_amount)
    elif should_sell:
        exchange.sell(symbol, trade_amount)
    else:
        print("No action needed.")


if __name__ == "__main__":
    main()
