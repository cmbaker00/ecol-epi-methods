from citation_data import *
import matplotlib.pyplot as plt
import numpy as np

def get_methods():
    return ['ethics','optim','costben','voi','adaptive','ibm','sdm','ensemble']

def file_names(method):
    ff = '{0}_fisheries'.format(method)
    fc = '{0}_cons'.format(method)
    fe = '{0}_epi'.format(method)
    return ff, fc, fe

def plot_citations_year(t, citations, mint = 1950, maxt = 2015):
    trange = (t <= 2015) & (t > 1950)
    plt.plot(t[trange], citations[trange])
    plt.show()

def year_x_citations(t, citations, num = 10):
    cum_citations = np.cumsum(citations)
    return t[cum_citations > 0][0]

def get_start_year_publications(method, num = 10):
    ff, fc, fe = file_names(method)
    tff, citationsff, papersff = get_citations_by_year(ff)
    tfc, citationsfc, papersfc = get_citations_by_year(fc)
    tfe, citationsfe, papersfe = get_citations_by_year(fe)
    ff_st = year_x_citations(tff, papersff)
    fc_st = year_x_citations(tfc, papersfc)
    fe_st = year_x_citations(tfe, papersfe)
    return ff_st, fc_st, fe_st

def get_all_start_years():
    opts = get_methods()
    out = {}
    for opt in opts:
        yrs = get_start_year_publications(opts)
        out[opt] = {'fish': yrs[0], 'cons': yrs[1], 'epi': yrs[2]}
    return out