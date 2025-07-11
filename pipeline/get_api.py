"""Script for getting API from steamworks."""

import time
import csv
import os
import re
from datetime import datetime

import requests
import pandas as pd

from utilities import get_logger, set_logger


STEAM_API_URL_ONE = "https://store.steampowered.com/appreviews/"

STEAM_API_URL_TWO = "?json=1&filter=recent&language=english&purchase_type=all&num_per_page=100&cursor="


def get_api_request(game_id: int = 1,
                    cursor: str = "*") -> dict:
    """Returns objects from a given API URL call.
    Repeated in loop to get all reviews."""
    logger = get_logger()

    local_steam_url = STEAM_API_URL_ONE + \
        str(game_id) + STEAM_API_URL_TWO + cursor
    response = requests.get(local_steam_url, timeout=10)
    if response.status_code != 200:
        logger.critical("Could not connect to Steam API.")
        raise ConnectionError("Could not connect to Steam API.")
    return response.json()


if __name__ == "__main__":
    print(get_api_request(420, "*"))
