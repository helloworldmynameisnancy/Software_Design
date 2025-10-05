import unittest
from unittest.mock import patch, Mock

from src.astronaut_names_webservice import get_response, parse_response, get_astronauts_names


class AstronautNamesWebservice(unittest.TestCase):
    def test_get_response_returns_response_from_the_webservice_for_astronauts_names(self):
        self.assertEqual(get_response().keys(), {'people', 'number', 'message'})

    def test_parse_response_returns_astronauts_names_for_ISS_from_the_given_sample_data(self):
        data = {
            "people": [
                {"craft": "ISS", "name": "Oleg Kononenko"},
                {"craft": "ISS", "name": "Nikolai Chub"},
                {"craft": "Tiangong", "name": "Li Guangsu"},
                {"craft": "Tiangong", "name": "Li Cong"}
            ],
            "number": 4,
            "message": "success"
        }

        self.assertEqual(parse_response(data), ["Oleg Kononenko", "Nikolai Chub"])

    def test_parse_response_returns_astronauts_names_for_ISS_from_another_sample_data(self):
        data = {
            "people": [
                {"craft": "ISS", "name": "Tracy Caldwell Dyson"}, 
                {"craft": "ISS", "name": "Matthew Dominick"}
            ], 
            "number": 2, 
            "message": "success"
        }

        self.assertEqual(parse_response(data), ["Tracy Caldwell Dyson", "Matthew Dominick"])

    def test_get_astronaut_names_calls_get_and_parse(self):
        data = {
            "people": [
                {"craft": "ISS", "name": "Tracy Caldwell Dyson"}, 
                {"craft": "ISS", "name": "Matthew Dominick"}
            ], 
            "number": 2, 
            "message": "success"
        }
        
        names = ["Tracy Caldwell Dyson", "Matthew Dominick"]

        mock_get_response = Mock(return_value=data)
        mock_parse_response = Mock(return_value=names)

        with patch("src.astronaut_names_webservice.get_response", mock_get_response), patch("src.astronaut_names_webservice.parse_response", mock_parse_response):
            response_names = get_astronauts_names()

            self.assertEqual(names, response_names)
            mock_get_response.assert_called_once()
            mock_parse_response.assert_called_once()

    def test_get_astronaut_names_throws_exception_if_get_error(self):
        mock_get_response = Mock(side_effect=Exception("astronaut_names_webservice error: failed to get response"))

        with patch("src.astronaut_names_webservice.get_response", mock_get_response), self.assertRaisesRegex(Exception, "astronaut_names_webservice error: failed to get response"):
            get_astronauts_names()

    def test_get_astronaut_names_throws_exception_if_parse_error(self):
        data = {
            "people": [
                {"craft": "ISS", "name": "Tracy Caldwell Dyson"}, 
                {"craft": "ISS", "name": "Matthew Dominick"}
            ], 
            "number": 2, 
            "message": "success"
        }

        mock_get_response = Mock(return_value=data)
        mock_parse_response = Mock(side_effect=Exception("astronaut_names_webservice error: failed to parse response"))

        with patch("src.astronaut_names_webservice.get_response", mock_get_response), patch("src.astronaut_names_webservice.parse_response", mock_parse_response), self.assertRaisesRegex(Exception, "astronaut_names_webservice error: failed to parse response"):
            get_astronauts_names()

if __name__ == "__main__":
    unittest.main()
