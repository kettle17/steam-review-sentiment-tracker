"""Contains all fixtures used for testing."""

import pytest
import pandas as pd
import os
from unittest.mock import patch


@pytest.fixture
def example_api_call_reviews():
    """An example review API call from the Steam API, calling two review items."""
    return {
        "success": 1,
        "query_summary": {
            "num_reviews": 2,
            "review_score": 9,
            "review_score_desc": "Overwhelmingly Positive",
            "total_positive": 15753,
            "total_negative": 503,
            "total_reviews": 16256
        },
        "reviews": [
            {
                "recommendationid": "198015818",
                "author": {
                    "steamid": "76561199434220432",
                    "num_games_owned": 260,
                    "num_reviews": 54,
                    "playtime_forever": 1200,
                    "playtime_last_two_weeks": 0,
                    "playtime_at_review": 1200,
                    "last_played": 1750745154
                },
                "language": "english",
                "review": "First playthrough took me just under 8 hours, I came back after however long it had been to finish up achievements and that playthrough rounded it out to 20 hours. 10/10, perfect cliffhanger, still waiting on hl3...\n(this game shouldn't be in tools lol)",
                "timestamp_created": 1750745311,
                "timestamp_updated": 1750745311,
                "voted_up": True,
                "votes_up": 1,
                "votes_funny": 0,
                "weighted_vote_score": "0.523809552192687988",
                "comment_count": 0,
                "steam_purchase": True,
                "received_for_free": False,
                "written_during_early_access": False,
                "primarily_steam_deck": False
            },
            {
                "recommendationid": "199675855",
                "author": {
                    "steamid": "76561199170729948",
                    "num_games_owned": 0,
                    "num_reviews": 18,
                    "playtime_forever": 478,
                    "playtime_last_two_weeks": 0,
                    "playtime_at_review": 478,
                    "last_played": 1719154872
                },
                "language": "english",
                "review": "it's the best at best. the pacing is good, theres a ♥♥♥♥♥♥♥♥ ton of enemies, and the strider fight gave me not aids. i can even bare finishing it. best game in the series.\n",
                "timestamp_created": 1752383288,
                "timestamp_updated": 1752383288,
                "voted_up": True,
                "votes_up": 0,
                "votes_funny": 0,
                "weighted_vote_score": 0.5,
                "comment_count": 0,
                "steam_purchase": True,
                "received_for_free": False,
                "written_during_early_access": False,
                "primarily_steam_deck": False
            }
        ],
        "cursor": "AoIFQGKAAAAAAAB888T1BQ=="
    }


@pytest.fixture
def example_api_call_details():
    """An example details API call calling details about ID 420."""
    return {
        "420": {
            "success": True,
            "data": {
                "type": "game",
                "name": "Half-Life 2: Episode Two",
                "steam_appid": 420,
                "required_age": 0,
                "is_free": False,
                "controller_support": "full",
                "dlc": [
                    323160
                ],
                "detailed_description": "Half-Life® 2: Episode Two is the second in a trilogy of new games created by Valve that extends the award-winning and best-selling Half-Life® adventure.<br />\r\n\t\t\t\t\tAs Dr. Gordon Freeman, you were last seen exiting City 17 with Alyx Vance as the Citadel erupted amidst a storm of unknown proportions. In Episode Two, you must battle and race against Combine forces as you traverse the White Forest to deliver a crucial information packet stolen from the Citadel to an enclave of fellow resistance scientists.<br />\r\n\t\t\t\t\tEpisode Two extends the award-winning Half-Life gameplay with unique weapons, vehicles, and newly-spawned creatures.",
                "about_the_game": "Half-Life® 2: Episode Two is the second in a trilogy of new games created by Valve that extends the award-winning and best-selling Half-Life® adventure.<br />\r\n\t\t\t\t\tAs Dr. Gordon Freeman, you were last seen exiting City 17 with Alyx Vance as the Citadel erupted amidst a storm of unknown proportions. In Episode Two, you must battle and race against Combine forces as you traverse the White Forest to deliver a crucial information packet stolen from the Citadel to an enclave of fellow resistance scientists.<br />\r\n\t\t\t\t\tEpisode Two extends the award-winning Half-Life gameplay with unique weapons, vehicles, and newly-spawned creatures.",
                "short_description": "Half-Life® 2: Episode Two is the second in a trilogy of new games created by Valve that extends the award-winning and best-selling Half-Life® adventure. As Dr. Gordon Freeman, you were last seen exiting City 17 with Alyx Vance as the Citadel erupted amidst a storm of unknown proportions.",
                "supported_languages": "English<strong>*</strong>, French<strong>*</strong>, German<strong>*</strong>, Russian<strong>*</strong>, Danish, Dutch, Finnish, Italian, Japanese, Korean, Norwegian, Polish, Portuguese - Portugal, Simplified Chinese, Spanish - Spain<strong>*</strong>, Swedish, Traditional Chinese<br><strong>*</strong>languages with full audio support",
                "header_image": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/header.jpg?t=1745368556",
                "capsule_image": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/capsule_231x87.jpg?t=1745368556",
                "capsule_imagev5": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/capsule_184x69.jpg?t=1745368556",
                "website": "http://www.whatistheorangebox.com/",
                "pc_requirements": {
                    "minimum": "\n\t\t\t<p><strong>Minimum: </strong>1.7 GHz Processor, 512MB RAM, DirectX&reg; 8.1 level Graphics Card (Requires support for SSE), Windows&reg; 7 (32/64-bit)/Vista/XP, Mouse, Keyboard, Internet Connection</p>\n\t\t\t<p><strong>Recommended: </strong>Pentium 4 processor (3.0GHz, or better), 1GB RAM, DirectX&reg; 9 level Graphics Card, Windows&reg; 7 (32/64-bit)/Vista/XP, Mouse, Keyboard, Internet Connection</p>\n\t\t\t"
                },
                "mac_requirements": {
                    "minimum": "<strong>Minimum: </strong>OS X version Leopard 10.5.8, Snow Leopard 10.6.3, 1GB RAM, NVIDIA GeForce 8 or higher, ATI X1600 or higher, or Intel HD 3000 or higher Mouse, Keyboard, Internet Connection"
                },
                "linux_requirements": [],
                "developers": [
                    "Valve"
                ],
                "publishers": [
                    "Valve"
                ],
                "packages": [
                    469
                ],
                "package_groups": [
                    {
                        "name": "default",
                        "title": "Buy Half-Life 2: Episode Two",
                        "description": "",
                        "selection_text": "Select a purchase option",
                        "save_text": "",
                        "display_type": 0,
                        "is_recurring_subscription": "false",
                        "subs": [
                            {
                                "packageid": 469,
                                "percent_savings_text": " ",
                                "percent_savings": 0,
                                "option_text": "The Orange Box - £16.75",
                                "option_description": "",
                                "can_get_free_license": "0",
                                "is_free_license": False,
                                "price_in_cents_with_discount": 1675
                            }
                        ]
                    }
                ],
                "platforms": {
                    "windows": True,
                    "mac": False,
                    "linux": True
                },
                "metacritic": {
                    "score": 90,
                    "url": "https://www.metacritic.com/game/pc/half-life-2-episode-two?ftag=MCD-06-10aaa1f"
                },
                "categories": [
                    {
                        "id": 2,
                        "description": "Single-player"
                    },
                    {
                        "id": 22,
                        "description": "Steam Achievements"
                    },
                    {
                        "id": 28,
                        "description": "Full controller support"
                    },
                    {
                        "id": 13,
                        "description": "Captions available"
                    },
                    {
                        "id": 67,
                        "description": "Camera Comfort"
                    },
                    {
                        "id": 68,
                        "description": "Custom Volume Controls"
                    },
                    {
                        "id": 78,
                        "description": "Adjustable Difficulty"
                    },
                    {
                        "id": 74,
                        "description": "Playable without Timed Input"
                    },
                    {
                        "id": 79,
                        "description": "Save Anytime"
                    },
                    {
                        "id": 69,
                        "description": "Stereo Sound"
                    },
                    {
                        "id": 65,
                        "description": "Subtitle Options"
                    },
                    {
                        "id": 70,
                        "description": "Surround Sound"
                    },
                    {
                        "id": 23,
                        "description": "Steam Cloud"
                    },
                    {
                        "id": 15,
                        "description": "Stats"
                    },
                    {
                        "id": 16,
                        "description": "Includes Source SDK"
                    },
                    {
                        "id": 14,
                        "description": "Commentary available"
                    },
                    {
                        "id": 62,
                        "description": "Family Sharing"
                    }
                ],
                "genres": [
                    {
                        "id": "1",
                        "description": "Action"
                    }
                ],
                "screenshots": [
                    {
                        "id": 0,
                        "path_thumbnail": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/ss_d2964cd9bd36406c4c3b2a90c21ab3d6ba0e6cca.600x338.jpg?t=1745368556",
                        "path_full": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/ss_d2964cd9bd36406c4c3b2a90c21ab3d6ba0e6cca.1920x1080.jpg?t=1745368556"
                    },
                    {
                        "id": 1,
                        "path_thumbnail": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/ss_1e01dc71d9abed491e89b1c1393164da6061f377.600x338.jpg?t=1745368556",
                        "path_full": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/ss_1e01dc71d9abed491e89b1c1393164da6061f377.1920x1080.jpg?t=1745368556"
                    },
                    {
                        "id": 2,
                        "path_thumbnail": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/ss_e69f62707e63558e234cd2e4f1a00315b6ed61bd.600x338.jpg?t=1745368556",
                        "path_full": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/ss_e69f62707e63558e234cd2e4f1a00315b6ed61bd.1920x1080.jpg?t=1745368556"
                    },
                    {
                        "id": 3,
                        "path_thumbnail": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/ss_35379dd632f3aa8a2c6cfa1878122d9c5a185ccb.600x338.jpg?t=1745368556",
                        "path_full": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/ss_35379dd632f3aa8a2c6cfa1878122d9c5a185ccb.1920x1080.jpg?t=1745368556"
                    },
                    {
                        "id": 4,
                        "path_thumbnail": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/ss_3ce99d4845ca60b795c5577372d25a382f2bb954.600x338.jpg?t=1745368556",
                        "path_full": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/420/ss_3ce99d4845ca60b795c5577372d25a382f2bb954.1920x1080.jpg?t=1745368556"
                    }
                ],
                "recommendations": {
                    "total": 34188
                },
                "achievements": {
                    "total": 23,
                    "highlighted": [
                        {
                            "name": "Acid Reflex",
                            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/420/ep2_kill_poisonantlion.jpg"
                        },
                        {
                            "name": "Get Some Grub",
                            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/420/ep2_kill_allgrubs.jpg"
                        },
                        {
                            "name": "Piñata Party",
                            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/420/ep2_break_allwebs.jpg"
                        },
                        {
                            "name": "Into the Breach",
                            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/420/ep2_beat_antlioninvasion.jpg"
                        },
                        {
                            "name": "Twofer",
                            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/420/ep2_beat_antlionguards.jpg"
                        },
                        {
                            "name": "Hit and Run",
                            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/420/ep2_kill_enemies_withcar.jpg"
                        },
                        {
                            "name": "Meet the Hunters",
                            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/420/ep2_beat_hunterambush.jpg"
                        },
                        {
                            "name": "Puttin' On a Clinic",
                            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/420/ep2_kill_chopper_nomisses.jpg"
                        },
                        {
                            "name": "Gunishment!",
                            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/420/ep2_kill_combinecannon.jpg"
                        },
                        {
                            "name": "Cache Checker",
                            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/420/ep2_find_allradarcaches.jpg"
                        }
                    ]
                },
                "release_date": {
                    "coming_soon": False,
                    "date": "10 Oct, 2007"
                },
                "support_info": {
                    "url": "",
                    "email": ""
                },
                "background": "https://store.akamai.steamstatic.com/images/storepagebackground/app/420?t=1745368556",
                "background_raw": "https://store.akamai.steamstatic.com/images/storepagebackground/app/420?t=1745368556",
                "content_descriptors": {
                    "ids": [],
                    "notes": "Half-Life 2: Episode Two includes violence throughout the game."
                },
                "ratings": {
                    "usk": {
                        "rating": "18"
                    },
                    "dejus": {
                        "rating_generated": "1",
                        "rating": "14",
                        "required_age": "14",
                        "banned": "0",
                        "use_age_gate": "0",
                        "descriptors": "Violência"
                    },
                    "steam_germany": {
                        "rating_generated": "1",
                        "rating": "16",
                        "required_age": "16",
                        "banned": "0",
                        "use_age_gate": "0",
                        "descriptors": "Drastische Gewalt"
                    }
                }
            }
        }
    }


@pytest.fixture
def incorrect_api_call_reviews():
    """An incorrect API call from the Steam reviews API.
    This happens when the entry does not exist."""
    return {
        "success": 1,
        "query_summary": {
            "num_reviews": 0
        },
        "reviews": [],
        "cursor": None
    }


@pytest.fixture
def incorrect_api_call_details():
    """An incorrect API call from the Steam details API.
    This happens when the entry does not exist."""
    return {
        "3232": {
            "success": False
        }
    }
