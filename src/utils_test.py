import unittest

import numpy as np
import pandas as pd

from src.utils import movement


class MovementTest(unittest.TestCase):
    @staticmethod
    def test_long_only():
        pd.testing.assert_series_equal(
            pd.Series([np.NAN, 10, 10]),
            movement(pd.DataFrame({
                "longitudeE7": [0, 10, 20],
                "latitudeE7": [0, 0, 0]
            })),
            check_exact=False
        )

    @staticmethod
    def test_lat_only():
        pd.testing.assert_series_equal(
            pd.Series([np.NAN, 10, 10]),
            movement(pd.DataFrame({
                "longitudeE7": [0, 0, 0],
                "latitudeE7": [0, 10, 20]
            })),
            check_exact=False
        )

    @staticmethod
    def test_diagonal():
        pd.testing.assert_series_equal(
            pd.Series([np.NAN, 14.1421, 14.1421]),
            movement(pd.DataFrame({
                "longitudeE7": [0, 10, 20],
                "latitudeE7": [0, 10, 20]
            })),
            check_exact=False
        )
