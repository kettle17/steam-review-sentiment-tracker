# pylint: skip-file

"""Test file for extract section of ETL."""
import pytest
import os
import json
from unittest.mock import patch, mock_open
from extract import (
    get_steam_api_request,
    get_all_reviews,
    run_extract
)


class TestGetSteamAPIRequest:
    """Tests for get_steam_api_request.
    True = reviews
    False = details"""

    def test_get_steam_api_request_reviews_id_invalid_type(self):
        """Test that checks if id is a valid int."""
        with pytest.raises(TypeError):
            get_steam_api_request('I am not an int', True)
        with pytest.raises(TypeError):
            get_steam_api_request('I am not an int', False)

    def test_get_steam_api_request_reviews_cursor_invalid_type(self):
        """Test that checks if cursor is a valid string."""
        with pytest.raises(TypeError):
            get_steam_api_request(3, True, 3)

    def test_get_steam_api_request_reviews_should_deny_negative(self):
        """Test that checks if id accepts negative values."""
        with pytest.raises(ValueError):
            get_steam_api_request(-58492573, True)
        with pytest.raises(ValueError):
            get_steam_api_request(-58492573, False)

    @patch('requests.get')
    def test_get_steam_api_request_reviews_should_deny_404(self, fake_requests):
        """Test that checks if function halts if it can't connect."""
        fake_requests.return_value.status_code = 404
        with pytest.raises(ConnectionError):
            get_steam_api_request(24234344, True)
        with pytest.raises(ConnectionError):
            get_steam_api_request(24234344, False)

    @patch('requests.get')
    def test_get_steam_api_request_reviews_correct(self, fake_requests):
        """Test that checks if function correctly functions for reviews."""
        fake_requests.return_value.status_code = 200
        fake_requests.return_value.response = json.dumps({'cool': 'cool'})
        assert get_steam_api_request(24234344, True)

    @patch('requests.get')
    def test_get_steam_api_request_reviews_correct_with_cursor(self, fake_requests):
        """Test that checks if function correctly functions for reviews with cursor."""
        fake_requests.return_value.status_code = 200
        fake_requests.return_value.response = json.dumps({'cool': 'cool'})
        assert get_steam_api_request(24234344, True, "hda2ne9")

    @patch('requests.get')
    def test_get_steam_api_request_details_correct(self, fake_requests):
        """Test that checks if function correctly functions for details."""
        fake_requests.return_value.status_code = 200
        fake_requests.return_value.response = json.dumps({'cool': 'cool'})
        assert get_steam_api_request(24234344, False)


class TestGetAllReviews:
    """Tests for get_all_reviews."""

    def test_get_api_request_start_date_invalid_type(self):
        """wadwad"""
        pass


class TestRunExtract:
    """Tests for run_extract."""

    def test_get_api_request_start_date_invalid_type(self):
        """wadwad"""
        pass


def test_if_extract_exists_should_exist():
    """Basic beginner test. If this test can't run, neither can the rest."""
    try:
        assert os.path.exists('pipeline/extract.py')
    except:
        assert os.path.exists('extract.py')
