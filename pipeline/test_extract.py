# pylint: skip-file

"""Test file for extract section of ETL."""
import pytest
import os
import json
from unittest.mock import patch, mock_open
from extract import (
    get_steam_api_request,
    fetch_api_data,
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
            get_steam_api_request('I am not an int', False)

    def test_get_steam_api_request_reviews_cursor_invalid_type(self):
        """Test that checks if cursor is a valid string."""
        with pytest.raises(TypeError):
            get_steam_api_request(3, True, 3)

    def test_get_steam_api_request_reviews_should_deny_negative(self):
        """Test that checks if id accepts negative values."""
        with pytest.raises(ValueError):
            get_steam_api_request(-58492573, True)
            get_steam_api_request(-58492573, False)

    @patch('requests.get')
    def test_get_steam_api_request_reviews_should_deny_404(self, fake_requests):
        """Test that checks if function halts if it can't connect."""
        fake_requests.return_value.status_code = 404
        with pytest.raises(ConnectionError):
            get_steam_api_request(24234344, True)
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


class TestFetchAPIData:
    """Tests for fetch_api_data."""

    @patch('extract.get_steam_api_request')
    def test_get_steam_api_request_is_correct_type_reviews(self, fake_get_request, example_api_call_reviews):
        """Test that correctly executes the function for reviews."""
        fake_get_request.return_value = example_api_call_reviews
        assert type(fetch_api_data(420, True)) == dict

    @patch('extract.get_steam_api_request')
    def test_get_steam_api_request_is_correct_type_details(self, fake_get_request, example_api_call_details):
        """Test that correctly executes the function for details."""
        fake_get_request.return_value = example_api_call_details
        assert type(fetch_api_data(420, False)) == dict

    def test_get_steam_api_request_invalid_type(self):
        """Test that checks if script halts on incorrect type parameter."""
        with pytest.raises(TypeError):
            fetch_api_data('I am not an int', True)
            fetch_api_data('I am not an int', False)

    def test_get_steam_api_request_is_negative_value(self):
        """Test that checks if id accepts negative values."""
        with pytest.raises(ValueError):
            fetch_api_data(-58492573, True)
            fetch_api_data(-58492573, False)

    @patch('extract.get_steam_api_request')
    def test_get_steam_api_request_incorrect_data_returned_reviews(self, fake_get_request, incorrect_api_call_reviews):
        """Test that checks if script halts if the format of review data is not as expected."""
        fake_get_request.return_value = incorrect_api_call_reviews
        with pytest.raises(ValueError):
            fetch_api_data(1749583860, True)

    @patch('extract.get_steam_api_request')
    def test_get_steam_api_request_incorrect_data_returned_details(self, fake_get_request, incorrect_api_call_details):
        """Test that checks if script halts if the format of detail data is not as expected."""
        fake_get_request.return_value = incorrect_api_call_details
        with pytest.raises(ValueError):
            fetch_api_data(3232, False)


class TestRunExtract:
    """Tests for run_extract."""

    def test_get_api_request_start_date_invalid_type(self):
        """wadwad"""
        pass
