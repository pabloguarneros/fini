class Option:

    ''' Option: contract giving the owner the right to buy/sell asset
                at specific time.
    '''

    def __init__(self,  underlying_asset,
                        time_to_maturity=1,
                        strike_price=0,
                        current_price=0):
                
        self.t = time_to_maturity #time to maturity
        self.k = strike_price #strike_price
        self.p0 = current_price #price at 0
        self.underlying_asset = underlying_asset
        self.type = "put" # long-put, long-call, short-put, short-call

    def __repr__(self):
        return f"Option: {self.time_to_maturity} Maturity // ${self.strike_price} Strike Price"

    def get_current_price(self):
        return self.current_price
    
    def get_future_price(self, t, r):
        ''' Calculate the future price of the option.
            Inputs:
                t (float): the time in years for which we calculate the price 
                r (float): rate of return
        '''
        return self.p0*(1+r)**t

    def get_payoff(self):
        ''' Get the payoff of the option.
        '''
        pass

    def get_today_price_w_binomial_option(self, u, d, r):
        q_u = ((1+r) - d) / (u - d) #probability of going up
        q_d = 1-q_u  #probability of going down
        c_u = 0  #price of call at u
        c_d = 0 #price of call at d
        print(self.underlying_asset.p0) #probability of going up
        return ((q_u*c_u+q_d+c_d)/(1+r))

class CallOption(Option):

    def __init__(self, t, k, p0=None):
        super().__init__(t, k, p0)

    def get_today_price_w_binomial_option(self, u, d, r):
        q_u = ((1+r) - d) / (u - d) #probability of going up
        q_d = 1-q_u  #probability of going down
        c_u = 0  #price of call at u
        c_d = 0 #price of call at d
        print(self.underlying_asset.p0) #probability of going up
        return ((q_u*c_u+q_d+c_d)/(1+r))


class PutOption(Option):
    def __init__(self, t, k, p0=None):
        super().__init__(t,k, p0)

class LongCallOption(CallOption):

    def __init__(self, t, k, p0=None):
        super().__init__(t,k, p0)

    def get_payoff(self, **kwargs):
        return max(0, kwargs["stock_price"] - self.k) 

class ShortCallOption(CallOption):

    def __init__(self, t, k, p0=None):
        super().__init__(t,k, p0)
    
    def get_payoff(self, **kwargs):
        return min(0, self.strike_price - kwargs["stock_price"]) 

class LongPutOption(PutOption):

    def __init__(self, t, k, p0=None):
        super().__init__(t,k, p0)
    
    def get_payoff(self, **kwargs):
        if self.type in ["long-put", "short-call"]:
            return max(0, self.strike_price - kwargs["stock_price"])
        elif self.type in ["long-call"]:
            return max(0, kwargs["stock_price"] - self.k) 

class ShortPutOption(PutOption):

    def __init__(self, t, k, p0=None):
        super().__init__(t,k, p0)
    
    def get_payoff(self, **kwargs):
        return min(0, kwargs["stock_price"]-self.strike_price)