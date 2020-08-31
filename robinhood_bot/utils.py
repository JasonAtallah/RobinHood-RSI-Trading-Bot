import logging
import os
import sys

from pyrh import Robinhood


def get_logger(name="rh_bot"):
    return logging.getLogger(name)


logger = get_logger()


def create_robinhood_instance(username=None, password=None):
    try:
        if not username:
            username = os.getenv("USERNAME")

        if not password:
            password = os.getenv("PASSWORD")

        rh = Robinhood()
        rh.login(username, password)

        return rh
    except Exception:
        logger.error("Failed to login, exiting...")
        sys.exit()


def get_delay():
    try:
        delay = os.getenv("DELAY_IN_SECONDS", 60)
        return int(delay)
    except ValueError:
        logger.warn("DELAY_IN_SECONDS is not a valid integer, defaulting to 60 seconds")
        return 60


def get_ticker_symbols():
    try:
        ticker_symbols = [
            ticker_symbol.strip()
            for ticker_symbol in os.getenv("TICKER_SYMBOLS").split(",")
        ]

        return ticker_symbols
    except Exception:
        logger.error("Failed to load ticker symbols, exiting...")
        sys.exit()


def shares_to_trade(ticker_symbol):
    return os.getenv(ticker_symbol, 1)