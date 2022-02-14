class MarketPortfolio:

    def __init__(self,
                expected_return=0,
                returns_stdev=0,
                risk_free_rate=0):

        self.expected_return = expected_return
        self.returns_stdev = returns_stdev
        self.risk_free_rate = risk_free_rate