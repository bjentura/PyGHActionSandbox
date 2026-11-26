import unittest
import numpy as np

from pyghactionsandbox.func import create_nan

class FuncTests(unittest.TestCase):

    def test_create_nan(self) -> None:
        self.assertTrue(np.isnan(create_nan()))

if __name__ == "__main__":
    unittest.main()
