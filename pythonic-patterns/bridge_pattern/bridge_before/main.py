from coinbase import Coinbase


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10

    # create the exchange
    exchange = Coinbase()

    exchange.buy(symbol, trade_amount)


if __name__ == "__main__":
    main()
