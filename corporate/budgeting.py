import numpy as np

def get_cost_of_capital(beta, rf, rm=None, rp=None):
    ''' Inputs:
            rm: market risk-return
            rp: risk-premium
            rf: risk-free rate
    '''
    r = None
    if rm != None:
        r = rf + beta*(rm-rf)
    elif rp != None:
        r = rf + beta*(rp)
    return r

def get_industry_beta(companies, industry):
    ''' Inputs:
            companies (array):
                - beta
                - weights
                    - asset:
                    - value:
            niche (str) of product to replicate
    '''
    betas = np.array([[company["beta"]] for company in companies])
    market_weights = [[] for _ in range(len(companies))]
    for i, company in enumerate(companies):
        weights = [weight for weight in company["weights"].values()]
        market_weights[i] = (weights)
    industry_betas_1 = np.linalg.inv(np.matrix(market_weights)) @ betas
    industry_betas = {}
    for i, given_industry in enumerate(companies[0]["weights"].keys()):
        industry_betas[given_industry] = industry_betas_1[i]
    return industry_betas[industry]

