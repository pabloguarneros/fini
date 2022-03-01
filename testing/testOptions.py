import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from assets.stocks import Stock
from assets.options import Option
import unittest

class TestPortfolio(unittest.TestCase):

    def test_get_current_price(self):
        stock = Stock(p0=12)
        option = Option(
            underlying_asset = stock,
            time_to_maturity=2,
            strike_price=1,
            current_price=2
        )
        self.assertEqual(option.get_current_price(),2)

if __name__ == "__main__":
    unittest.main()