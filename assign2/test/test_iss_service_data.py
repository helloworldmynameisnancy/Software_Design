import unittest

from src.iss_service_data import get_location, get_astronaut

class ISSServiceData(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_get_location_returns_time_and_location_that_the_service_returns(self):
        iss_location_service = lambda: ("05:17AM", "Houston, TX")

        self.assertEqual(get_location(iss_location_service), ("05:17AM", "Houston, TX"))

    def throw(self, message): 
        raise Exception(message)
    
    def test_get_location_returns_network_error_if_the_service_throws_an_exception(self):
        iss_location_service = lambda: self.throw("network error: service unreachable")

        self.assertEqual(get_location(iss_location_service), "network error: service unreachable")

    def test_get_location_returns_service_failed_if_the_service_throws_an_exception(self):
        iss_location_service = lambda: self.throw("service failed to respond")

        self.assertEqual(get_location(iss_location_service), "service failed to respond")

    def test_get_astronaut_returns_empty_list_if_service_returns_empty_list(self):
        iss_astronaut_service = lambda: []

        self.assertEqual(get_astronaut(iss_astronaut_service), [])
    
    def test_get_astronaut_returns_list_with_one_name_if_service_returns_list_with_one_name(self):
        iss_astronaut_service = lambda: ["Oleg Chub"]

        self.assertEqual(get_astronaut(iss_astronaut_service), ["Oleg Chub"])

    def test_get_astronaut_returns_list_with_two_names_if_service_returns_list_with_two_names_sorted(self):
        iss_astronaut_service = lambda: ["Oleg Chub", "Nikolai Kononenko"]

        self.assertEqual(get_astronaut(iss_astronaut_service), ["Oleg Chub", "Nikolai Kononenko"])

    def test_get_astronaut_returns_list_with_two_sorted_names_if_service_returns_list_with_two_names_unsorted(self):
        iss_astronaut_service = lambda: ["Nikolai Kononenko", "Oleg Chub"]

        self.assertEqual(get_astronaut(iss_astronaut_service), ["Oleg Chub", "Nikolai Kononenko"])

    def test_get_astronauts_returns_list_with_two_names_in_sorted_order_if_service_returns_a_list_with_two_names_where_the_last_names_same_but_first_names_different_and_in_unsorted_order(self):
        iss_astronaut_service = lambda: ["Oleg Chub", "Nikolai Chub"]

        self.assertEqual(get_astronaut(iss_astronaut_service), ["Nikolai Chub", "Oleg Chub"])

    def test_get_astronaut_returns_list_with_two_names_in_sorted_order_if_service_returns_list_with_two_names_unsorted_where_one_name_includes_three_parts(self):
        iss_astronaut_service = lambda: ["Tracy Caldwell Dyson", "Oleg Chub"]

        self.assertEqual(get_astronaut(iss_astronaut_service), ["Oleg Chub", "Tracy Caldwell Dyson"])
    
    def test_get_astronaut_service_returns_service_failed_if_the_service_throws_an_exception(self):
        iss_astronaut_service = lambda: self.throw("service failed to respond")

        self.assertEqual(get_astronaut(iss_astronaut_service), "service failed to respond")

    def test_get_astronaut_service_returns_network_error_if_the_service_throws_an_exception(self):
        iss_astronaut_service = lambda: self.throw("network error: service unreachable")

        self.assertEqual(get_astronaut(iss_astronaut_service), "network error: service unreachable")
        
if __name__ == "__main__":
    unittest.main()
