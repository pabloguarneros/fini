import matplotlib.pyplot as plt
import numpy as np

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
        return self.p0
    
    def get_future_price(self, t, r):
        ''' Calculate the future price of the option.
            Inputs:
                t (float): the time in years for which we calculate the price 
                r (float): rate of return
        '''
        return self.p0*(1+r)**t

    def get_payoff(self, stock_price):
        if self.type in ["long-put", "short-call"]:
            return max(0, self.k - stock_price)
        elif self.type in ["long-call", "short-put"]:
            return max(0, stock_price - self.k) 

    def get_today_price_w_binomial_option(self, u, d, r):
        q_u = ((1+r) - d) / (u - d) #probability of going up
        q_d = 1-q_u  #probability of going down
        c_u = 0  #price of call at u
        c_d = 0 #price of call at d
        print(self.underlying_asset.p0) #probability of going up
        return ((q_u*c_u+q_d+c_d)/(1+r))


    def build_payoff_diagram(self, price_range, *args):
        stock_prices = np.arange(
                            price_range[0],
                            price_range[1],
                            (price_range[1]-price_range[0])//10)
        if args:
            args.append(self)
            payoff_calc = lambda e: sum([option.get_payoff(stock_price=e) for option in args])
        else:
            payoff_calc = lambda e: self.get_payoff(stock_price=e)

        payoff = list(map(payoff_calc,stock_prices))
        plt.title(f"Payoff Diagram for \n {[arg for arg in args]}")
        plt.plot(stock_prices, payoff)
        plt.xlabel('Stock Price')
        plt.ylabel('Payoffs')
        x1,x2, _, _ = plt.axis()  
        plt.axis((x1,x2,-200,200))
        plt.axhline(y = 0, color="black")
        plt.show()