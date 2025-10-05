import unittest
from unittest.mock import patch, Mock

from src.location_webservice import get_response, parse_response, get_location


class LocationWebservice(unittest.TestCase):
    def test_get_location_response_returns_response_from_the_webservice_for_ISS_time_and_location(self):
            self.assertEqual(get_response().keys(), {'message', 'timestamp', 'iss_position'})

    def test_parse_response_returns_location_and_timestamp_for_ISS_from_the_given_sample_data(self):
        data = {
             "message": "success", 
             "iss_position": {"longitude": "84.3677", "latitude": "49.3340"}, 
             "timestamp": 1740955361 
        }

        self.assertEqual(parse_response(data), {"latitude": "49.3340", "longitude": "84.3677", "timestamp": 1740955361})

    def test_parse_response_returns_location_and_timestamp_for_ISS_from_another_given_sample_data(self):
        data = {
             "message": "success", 
             "iss_position": {"longitude": "20.1234", "latitude": "40.1234"}, 
             "timestamp": 1740955361 
        }

        self.assertEqual(parse_response(data), {"latitude": "40.1234", "longitude": "20.1234", "timestamp": 1740955361})
    
    def test_get_location_calls_parse_response_and_get_response(self):
        data = {
             "message": "success", 
             "iss_position": {"longitude": "-95.3701", "latitude": "29.7601"}, 
             "timestamp": 1740955361
        }

        location_and_timestamp = {"latitude": "29.7601", "longitude": "-95.3701", "timestamp": 1740955361}

        mock_get_response = Mock(return_value=data)
        mock_parse_response = Mock(return_value=location_and_timestamp)

        with patch("src.location_webservice.get_response", mock_get_response), patch("src.location_webservice.parse_response", mock_parse_response):
            response_location_and_time = get_location()

            self.assertEqual(response_location_and_time, {"place": "Houston, TX", "central_time": "04:42 PM"})
            mock_get_response.assert_called_once()
            mock_parse_response.assert_called_once()
    
    def test_get_location_returns_the_time_in_CT_instead_of_the_time_stamp(self):
        data = {
             "message": "success", 
             "iss_position": {"longitude": "-95.3701", "latitude": "29.7601"}, 
             "timestamp": 1740955361 
        }

        location_and_timestamp = {"latitude": "29.7601", "longitude": "-95.3701", "timestamp": 1740955361}

        mock_get_response = Mock(return_value=data)
        mock_parse_response = Mock(return_value=location_and_timestamp)

        with patch("src.location_webservice.get_response", mock_get_response), patch("src.location_webservice.parse_response", mock_parse_response):
            response_location_and_time = get_location()

            self.assertEqual(response_location_and_time, {"place": 'Houston, TX', "central_time": "04:42 PM"})
    
    def test_get_location_returns_the_place_with_city_and_state_of_ISS(self):
        data = {
             "message": "success", 
             "iss_position": {"longitude": "-95.3701", "latitude": "29.7601"}, 
             "timestamp": 1740955361 
        }

        location_and_timestamp = {"latitude": "29.7601", "longitude": "-95.3701", "timestamp": 1740955361}

        mock_get_response = Mock(return_value=data)
        mock_parse_response = Mock(return_value=location_and_timestamp)

        with patch("src.location_webservice.get_response", mock_get_response), patch("src.location_webservice.parse_response", mock_parse_response):
            response_location_and_time = get_location()

            self.assertEqual(response_location_and_time, {"place": 'Houston, TX', "central_time": "04:42 PM"})

    def test_get_location_returns_unknown_location_if_ISS_location_unknown(self):
        data = {
             "message": "success", 
             "iss_position": {"longitude": "-95.3701", "latitude": "29.7601"}, 
             "timestamp": 1740955361 
        }

        location_and_timestamp = {"latitude": "-39.4159", "longitude": "-146.9932", "timestamp": 1740955361}

        mock_get_response = Mock(return_value=data)
        mock_parse_response = Mock(return_value=location_and_timestamp)

        with patch("src.location_webservice.get_response", mock_get_response), patch("src.location_webservice.parse_response", mock_parse_response):
            response_location_and_time = get_location()

            self.assertEqual(response_location_and_time, {"place": 'Unknown Location', "central_time": "04:42 PM"})

    def test_get_location_throws_exception_if_get_error(self):
        mock_get_response = Mock(side_effect=Exception("location_webservice error: failed to get response"))

        with patch("src.location_webservice.get_response", mock_get_response), self.assertRaisesRegex(Exception, "location_webservice error: failed to get response"):
            get_location()

    def test_get_location_throws_exception_if_parse_error(self):
        data = {
             "message": "success", 
             "iss_position": {"longitude": "-95.3701", "latitude": "29.7601"}, 
             "timestamp": 1740955361 
        }

        mock_get_response = Mock(return_value=data)
        mock_parse_response = Mock(side_effect=Exception("location_webservice error: failed to parse response"))

        with patch("src.location_webservice.get_response", mock_get_response), patch("src.location_webservice.parse_response", mock_parse_response), self.assertRaisesRegex(Exception, "location_webservice error: failed to parse response"):
            get_location()

if __name__ == "__main__":
    unittest.main()
