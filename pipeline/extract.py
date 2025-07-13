"""Script for extracting the Steam API from a specified ID."""

import time
import csv
import os
import re
from datetime import datetime

import requests
import pandas as pd
import urllib
import argparse
import tqdm

from utilities import get_logger, set_logger


STEAM_API_URL_ONE = "https://store.steampowered.com/appreviews/"
STEAM_API_URL_TWO = "?json=1&filter=recent&language=english&purchase_type=all&num_per_page=100&cursor="

STEAM_API_URL_THREE = "https://store.steampowered.com/api/appdetails?appids="


def get_steam_api_request_reviews(game_id: int = 420,
                                  cursor: str = "*") -> dict:
    """Returns review json object from a given Steam app URL call.
    Repeated in loop to get all reviews."""
    logger = get_logger()

    local_steam_url = STEAM_API_URL_ONE + \
        str(game_id) + STEAM_API_URL_TWO + cursor
    response = requests.get(local_steam_url, timeout=10)
    if response.status_code != 200:
        logger.critical("Could not connect to Steam API.")
        raise ConnectionError("Could not connect to Steam API.")
    return response.json()


def get_steam_api_request_details(game_id: int = 420) -> dict:
    """Returns details about given steam ID (title, developers)
    Repeated in loop to get all reviews."""
    logger = get_logger()

    local_steam_url = STEAM_API_URL_THREE + str(game_id)
    response = requests.get(local_steam_url, timeout=10)
    if response.status_code != 200:
        logger.critical("Could not connect to Steam API.")
        raise ConnectionError("Could not connect to Steam API.")
    return response.json()


def get_all_reviews(game_id: int = 1) -> dict:
    """Retrieves basic data & review data in increments of 100.
    Stops when all reviews are retrieved."""
    logger = get_logger()
    all_reviews = []

    initial_request_reviews = get_steam_api_request_reviews(game_id, "*")
    if initial_request_reviews["success"] == "8":
        return None
    request_details = get_steam_api_request_details(game_id)[
        str(game_id)]
    if not request_details["success"]:
        return None
    request_details = request_details["data"]

    logger.info("Retrieving all reviews from id %s, '%s'...",
                game_id, request_details["name"])

    query_summary = initial_request_reviews["query_summary"]

    total_reviews = query_summary["total_reviews"]
    total_reviews_in_req = query_summary["num_reviews"]
    all_reviews += initial_request_reviews["reviews"]
    cursor_returned = urllib.parse.quote_plus(
        initial_request_reviews["cursor"])

    current_review_num = total_reviews_in_req

    while total_reviews_in_req > 0:
        if len(all_reviews) > 10000:
            logger.info("Stopping retrieval as review count exceeds 10000.")
            break
        next_req = get_steam_api_request_reviews(game_id, cursor_returned)
        total_reviews_in_req = next_req["query_summary"]["num_reviews"]
        all_reviews += next_req["reviews"]
        cursor_returned = urllib.parse.quote_plus(next_req["cursor"])
        current_review_num += total_reviews_in_req

    logger.info("Found %s reviews.", len(all_reviews))

    return {
        "title": request_details["name"],
        "description": request_details["short_description"],
        "header_image": request_details["header_image"],
        "developers": request_details["developers"],
        "publishers": request_details["publishers"],
        "total_reviews": total_reviews,
        "average_review_score": query_summary["review_score"],
        "review_desc": query_summary["review_score_desc"],
        "total_positive": query_summary["total_positive"],
        "total_negative": query_summary["total_negative"],
        "reviews": all_reviews,
    }


def run_extract() -> dict:
    """Runs extract script and returns found reviews."""
    logger = get_logger()
    args = get_terminal_args()
    if args:
        reviews = get_all_reviews(args.id)
    else:
        reviews = get_all_reviews(866570)
    if reviews:
        return reviews
    else:
        logger.critical("Game not found.")


def get_terminal_args() -> argparse.Namespace:
    """Capture the arguments from the terminal."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--id",
                        help="enter a steam id")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    set_logger()
    run_extract()
