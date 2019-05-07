import unittest
from location import location_name


class CityCountryTestCase(unittest.TestCase):
    """Tests for location.py."""

    def test_city_country(self):
        """Do location such as "Lviv, Ukraine" work? """
        your_location = location_name("lviv", "ukraine")
        self.assertEqual(your_location, "Lviv, Ukraine")

    def test_city_country_population(self):
        """Do location such as "Lviv, Ukraine - 1000000" work? """
        your_location = location_name("lviv", "ukraine", "123")
        self.assertEqual(your_location, "Lviv, Ukraine - 123")


if __name__ == '__main__':
    unittest.main()
