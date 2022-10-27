from avg_trading_bot import should_buy_avg, should_sell_avg
from coinbase import buy, get_prices, sell
from trading import run_bot

SYMBOL = "BTC/USD"
TRADE_AMOUNT = 10


def main() -> None:
    run_bot(
        get_prices, should_buy_avg, should_sell_avg, buy, sell, SYMBOL, TRADE_AMOUNT
    )


if __name__ == "__main__":
    main()
