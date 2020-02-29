import timeit
import unittest

from src.tools.visualising import load_or_get_belgium_roads


class CachingBelgianRoadsTest(unittest.TestCase):
    @staticmethod
    def time_loading():
        start = timeit.timeit()
        load_or_get_belgium_roads(repository_root_location="./")
        end = timeit.timeit()
        return end - start

    def test_loading_belgian_roads_speed(self):
        self.assertGreater(self.time_loading(), self.time_loading() * 10)
