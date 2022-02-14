def get_shares_of_stock(cu, cd, u, d, s0):
    ''' Inputs:
        cu(float): cash flow of option at up node
        cd(float): cash flow of option at down node
        u: stock price assumed at up node
        d: stock price assumed at down node
        s0:
    '''
    return (cu-cd)/((u-d)*s0)

def get_dollars_in_riskless_bonds(cu, cd, u, d, r):
    return (1/(1+r))*((u*cd-d*cu)/(u-d))