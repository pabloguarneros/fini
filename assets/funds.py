class ETF:

    def __init__(self, name, r=0, stdev=0):

        self.name = name
        self.r = r
        self.stdev = stdev

    def __repr__(self):
        return self.name

    def get_variance(self,other,correlation):
        return self.stdev*other.stdev*correlation