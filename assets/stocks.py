import math

class Stock:

    def __init__(self, p0 = None,
                market_beta=0, expected_return=0,
                return_volatility=0):
        self.p0 = p0
        self.b = market_beta
        self.r = expected_return
        self.stdev = return_volatility

    def get_market_alpha(self, market_portfolio):
        ''' Get alpha, or the difference betwen expected return
            and expected return under CAPM.
        '''
        mp = market_portfolio
        return_under_market = mp.risk_free_rate + self.b*(mp.expected_return-mp.risk_free_rate)
        return self.r - return_under_market

    def get_market_stdev(self, market_portfolio):
        mp = market_portfolio
        return math.sqrt(self.stdev**2-self.b**2*mp.returns_stdev**2)

    def get_idiosyncratic_volatility(self, market_portfolio):
        volatility_under_market = self.get_market_stdev(market_portfolio)
        return self.stdev - volatility_under_market
