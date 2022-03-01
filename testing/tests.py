import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from portfolio.main import Portfolio
from assets.funds import ETF
import unittest

class TestPortfolio(unittest.TestCase):

    def test_two_assets_return(self):
        """ Test portfolio return for two portfolio assets. """

        abc = ETF("ABC", r=0.05,stdev=0.1)
        xyz = ETF("XYZ", r=0.2,stdev=0.4)
        portfolio = Portfolio()
        portfolio.load_assets(  [abc,xyz],
                                [0.4, 0.6],
                                [[0.1*0.1,-0.02],[-0.02,0.4*0.4]])

        self.assertAlmostEqual(portfolio.get_return(),0.14,2)

    def test_two_assets_stdev(self):
        """ Test portfolio standard deviation for two portfolio assets. """

        abc = ETF("ABC", r=0.05,stdev=0.1)
        xyz = ETF("XYZ", r=0.2,stdev=0.4)
        portfolio = Portfolio()
        portfolio.load_assets(  [abc,xyz],
                                [0.4, 0.6],
                                [[0.1*0.1,-0.02],[-0.02,0.4*0.4]])

        portfolio_stdev = portfolio.get_variance()**(1/2)
        self.assertAlmostEqual(portfolio_stdev,0.22,2)

    def test_three_assets_return(self):
        """ Test portfolio return for three portfolio assets. """

        A = ETF("A", r=0.05,stdev=0.1)
        B = ETF("B", r=0.2,stdev=0.4)
        C = ETF("B", r=0.2,stdev=0.4)

        portfolio = Portfolio()
        portfolio.load_assets(  [A,B,C],
                                [1/3,1/3,1/3],
                                [
                                    [A.stdev*A.stdev, A.get_variance(B,-0.5), 0],
                                    [B.get_variance(A,-0.5),B.stdev*B.stdev,0],
                                    [0,0,C.stdev*C.stdev]
                                ])

        self.assertAlmostEqual(portfolio.get_return(), 0.15, 2)

    def test_three_assets_stdev(self):
        """ Test portfolio standard deviation for three portfolio assets. """

        A = ETF("A", r=0.05,stdev=0.1)
        B = ETF("B", r=0.2,stdev=0.4)
        C = ETF("B", r=0.2,stdev=0.4)

        portfolio = Portfolio()
        portfolio.load_assets(  [A,B,C],
                                [1/3,1/3,1/3],
                                [
                                    [A.stdev*A.stdev, A.get_variance(B,-0.5), 0],
                                    [B.get_variance(A,-0.5),B.stdev*B.stdev,0],
                                    [0,0,C.stdev*C.stdev]
                                ])

        portfolio_stdev = portfolio.get_variance()**(1/2)
        self.assertAlmostEqual(portfolio_stdev,0.18,2)

if __name__ == "__main__":
    unittest.main()