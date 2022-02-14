from sympy import symbols, solve
from scipy import optimize

class Asset:

    def __init__(self, underlying):
        self.underlying = underlying

    def __getattr__(self, item):
        return getattr(self.underlying, item)

    def set_weight(self, new_weight):
        self.weight = new_weight
    
    def __repr__(self):
        return self.underlying.name

class Portfolio:

    def __init__(self, expected_return=0):
        self.assets = []
        self.covariance_matrix = []
        self.expected_return = expected_return

    def load_assets(self, assets, weights, covariance_matrix):
        for asset1, w in zip(assets,weights):
            asset = Asset(asset1)
            asset.set_weight((w))
            self.assets.append(asset)

        self.covariance_matrix = covariance_matrix

    def set_return(self):

        avg_return = 0

        for asset in self.assets:
            avg_return += asset.weight*asset.r

        self.expected_return = avg_return
        
        return self.expected_return
            
    def get_variance(self):
        ''' To do: also account for negative correlation
        '''

        variance = 0

        for asset in self.assets:
            variance += (asset.weight**2)*(asset.stdev**2)
        
        for x, assetx in enumerate(self.assets[:len(self.assets)//2]):
            for y1, assety in enumerate(self.assets[len(self.assets)//2:]):
                if assetx != assety:
                    y = y1 + len(self.assets)//2
                    variance += 2*assetx.weight*assety.weight*self.covariance_matrix[x][y]
       
        return variance

    def optimize_weight_given_return(self,desired_return):

        if len(self.assets) == 2:
            a = self.assets[0].r
            b = self.assets[1].r
            return (desired_return-b)/(a-b) # desired w for a

    def optimize_weight_given_volatily(self,desired_volatility):

        if len(self.assets) == 2:
            variance = desired_volatility**2
            w = symbols('w')
            a = self.assets[0].stdev
            b = self.assets[1].stdev
            expr = (w**2)*(a**2)+((1-w)**2*b**2)+(2*w*(1-w)*self.covariance_matrix[0][1])-variance
            solutions = solve(expr)
            return solutions

    def get_min_variance(self):
        a = self.assets[0].stdev
        b = self.assets[1].stdev
        def f(w):
            return (w**2)*(a**2)+((1-w)**2*b**2)+(2*w*(1-w)*self.covariance_matrix[0][1])
        optimize.fmin(f)
        #variance shifts with the weight of change in stdev / change in w

    def get_sharpe_ratio(self, riskless_return):
        return (self.get_return()-riskless_return)/self.get_variance()


    def get_beta(self, market_portfolio):
        ''' Find beta of other porfolio given E[rp] = rf + Bp(E[rm]-rf)
        '''
        return (self.expected_return - market_portfolio.risk_free_rate)\
                /(market_portfolio.expected_return-market_portfolio.risk_free_rate)

    def get_stdev(self, market_portfolio):
        mp = market_portfolio
        market_weight = (self.expected_return - mp.risk_free_rate)/(mp.expected_return-mp.risk_free_rate)
        return market_weight*mp.returns_stdev

    def get_market_correlation(self, market_portfolio):
        return (self.get_beta(market_portfolio)*market_portfolio.returns_stdev)/self.get_stdev(market_portfolio)
