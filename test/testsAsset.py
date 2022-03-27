import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from assets.options import LongCallOption
from assets.stocks import Stock
import unittest

class TestOptions(unittest.TestCase):

    def test_a(self):

         self.assertAlmostEqual(portfolio_stdev,0.22,2)

if __name__ == "__main__":
    unittest.main()