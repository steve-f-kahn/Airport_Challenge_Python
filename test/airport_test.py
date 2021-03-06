import unittest
import sys
import os

if sys.path.count(os.getcwd) == 0 :
    sys.path.append(os.getcwd)

from lib.airport import Airport
from lib.weather import Weather

class TestAirport(unittest.TestCase):
    def test_airport_lets_plane_land_when_sunny(self):
        airport = Airport()
        airport.landPlane("Plane")
        self.assertEqual(airport.hanger.count("Plane"), 1)

    def test_airport_lets_plane_take_off_when_sunny(self):
        airport = Airport()
        airport.landPlane("Plane")
        airport.takeOffPlane("Plane")
        self.assertEqual(airport.hanger.count("Plane"), 0)

    def test_airport_does_not_let_plane_land_when_stormy(self):
        airport = Airport(Weather(99))
        with self.assertRaises(RuntimeError):
            airport.landPlane("Plane")

    def test_airport_does_not_let_plane_take_off_when_stormy(self):
        airport = Airport(Weather(1))
        airport.landPlane("Plane")
        airport.updateWeather(Weather(99))
        with self.assertRaises(RuntimeError):
            airport.takeOffPlane("Plane")

    def test_airport_default_capacity(self):
        airport = Airport()
        self.assertEqual(airport.capacity, 1)

    def test_airport_set_capacity(self):
        airport = Airport(capacity=5)
        self.assertEqual(airport.capacity, 5)

    def test_airport_does_not_allow_plane_to_land_when_at_capacity(self):
        airport = Airport()
        airport.landPlane("Plane")
        with self.assertRaises(RuntimeError):
            airport.landPlane("Plane2")

     
if __name__ == '__main__':
    unittest.main()
