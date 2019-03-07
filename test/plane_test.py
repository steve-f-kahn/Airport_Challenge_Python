import unittest
import sys
import os

if sys.path.count(os.getcwd) == 0 :
    sys.path.append(os.getcwd)

from lib.plane import Plane

class TestPlane(unittest.TestCase):

    def test_plane_is_flying_when_created(self):
        plane = Plane()
        self.assertEqual(plane.flying, True)

    def test_plane_lands_at_aiprot(self):
        plane = Plane()
        plane.land("Heathrow")
        self.assertEqual(plane.flying, False)

    def test_plane_take_off_from_airport(self):
        plane = Plane()
        plane.land("Heathrow")
        plane.takeoff("Heathrow")
        self.assertEqual(plane.flying, True)

if __name__ == '__main__' :
    unittest.main()
