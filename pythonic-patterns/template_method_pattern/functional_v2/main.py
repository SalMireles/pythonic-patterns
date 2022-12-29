from bitcoin import BitcoinTradingEngine
from ethereum import EthereumTradingEngine
from simple_strategy import SimpleStrategy
from trading_bot import trade


def main():
    strategy = SimpleStrategy()

    bitcoin_trader = BitcoinTradingEngine()
    trade(bitcoin_trader, strategy)

    ethereum_trader = EthereumTradingEngine()
    trade(ethereum_trader, strategy)


if __name__ == "__main__":
    main()
