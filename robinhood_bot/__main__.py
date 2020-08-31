import os
import time


from robinhood_bot.configuration import init
from robinhood_bot.utils import (
    create_robinhood_instance,
    get_delay,
    get_logger,
    get_ticker_symbols,
    shares_to_trade,
)

logger = get_logger()


def do_something(ticker_symbol):
    print("ticker_symbol", ticker_symbol)
    shares = shares_to_trade(ticker_symbol)


def start():
    init()

    delay = get_delay()
    ticker_symbols = get_ticker_symbols()
    rh = create_robinhood_instance()

    while True:
        for ticker_symbol in ticker_symbols:
            do_something(ticker_symbol)

        logger.debug(f"Sleeping for {delay}")
        time.sleep(delay)


if __name__ == "__main__":
    start()
