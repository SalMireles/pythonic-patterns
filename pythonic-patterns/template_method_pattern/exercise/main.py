from bitcoin import BitcoinTradingEngine
from ethereum import EthereumTradingEngine
from trading_bot import trade


def main():
    bitcoin_trader = BitcoinTradingEngine()
    trade(bitcoin_trader)

    ethereum_trader = EthereumTradingEngine()
    trade(ethereum_trader)


if __name__ == "__main__":
    main()
