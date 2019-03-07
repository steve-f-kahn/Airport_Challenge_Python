import unittest
import sys
import os

from lib.weather import Weather


if sys.path.count(os.getcwd) == 0 :
    sys.path.append(os.getcwd)

class TestWeather(unittest.TestCase) :

    def test_stormy(self) :
        weather = Weather(99)
        self.assertEqual(weather.storm, True)

    def test_sunny98(self) :
        weather = Weather(98)
        self.assertEqual(weather.storm, False)

    def test_sunny1(self) :
        weather = Weather(1)
        self.assertEqual(weather.storm, False)

if __name__ == '__main__':
    unittest.main()
