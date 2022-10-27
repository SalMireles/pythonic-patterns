from avg_trading_bot import should_buy_avg, should_sell_avg
from coinbase import buy, get_prices, sell


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10

    should_buy = should_buy_avg(symbol, get_prices)
    should_sell = should_sell_avg(symbol, get_prices)
    if should_buy:
        buy(symbol, trade_amount)
    elif should_sell:
        sell(symbol, trade_amount)
    else:
        print("No action needed.")


if __name__ == "__main__":
    main()
