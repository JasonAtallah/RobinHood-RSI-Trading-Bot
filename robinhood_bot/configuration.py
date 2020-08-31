import logging
import os
import sys

from dotenv import load_dotenv

from robinhood_bot.utils import get_logger

logger = get_logger()


def _configure_logger():
    """
    Configures a logger that can be used in the entire application.
    """
    level = int(os.getenv("LOGGING_LEVEL", 0))
    logging.basicConfig(
        format="[%(name)s][%(asctime)s][%(levelname)s]: %(message)s", level=level
    )


def _load_dotenv():
    """
    Parses environment variables from .env file into environment variabls
    """
    dotenv_path = os.path.join(os.getcwd(), ".env")
    load_dotenv(dotenv_path=dotenv_path)


def _validate_env(required_env_vars=["USERNAME", "PASSWORD", "TICKER_SYMBOLS"]):
    """
    Ensures all the required environment variables are present before the application runs
    """
    for env_var_name in required_env_vars:
        env_var = os.getenv(env_var_name)

        if bool(env_var) == False:
            logger.error(f"{env_var_name} is required")
            sys.exit()


def init():
    _load_dotenv()
    _configure_logger()
    logger.debug("dotenv loaded")
    logger.debug("logger initialized")
    _validate_env()
