"""Bridge Pattern Implementation.

the trading bot ABC has specific trading subclasses.

The exchange ABC has specific exchange subclasses.

The trading bot ABC has the link for the exchange serving as the bridge!

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
