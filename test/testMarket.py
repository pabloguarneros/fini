import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from market.market import Market
from assets.options import Option
from assets.stocks import Stock
import unittest

class TestMarket(unittest.TestCase):

    def setUp(self):
        stock = Stock()
        optionA = Option(stock,time_to_maturity=1/4,strike_price=40,current_price=2)
        optionB = Option(stock,time_to_maturity=1/4,strike_price=50,current_price=5)
        optionC = Option(stock,time_to_maturity=1/4,strike_price=60,current_price=9)
        optionD = Option(stock,time_to_maturity=1/4,strike_price=70,current_price=12)
        self.options = [optionA,optionB,optionC,optionD]

    def test_add(self):
        ''' Test adding options to the market '''
        m = Market()
        m.add(self.options)
        self.assertTrue((len(m.stocks),len(m.options)) == (0,4))

if __name__ == "__main__":
    unittest.main()