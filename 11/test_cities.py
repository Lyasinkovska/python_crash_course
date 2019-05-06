import unittest
from location import location_name


class CityCountryTestCase(unittest.TestCase):
    """Tests for location.py."""

    def test_city_country(self):
        """Do location such as "Kyiv, Ukraine" work? """
        your_location = location_name("Lviv", "Ukraine")
        self.assertEqual(your_location, "Lviv, Ukraine")


if __name__ == '__main__':
    unittest.main()
