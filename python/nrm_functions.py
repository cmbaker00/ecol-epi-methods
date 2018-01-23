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
        yrs = get_start_year_publications(opt)
        out[opt] = {'fish': yrs[0], 'cons': yrs[1], 'epi': yrs[2]}
    return out

def get_earliest_year():
    opts = get_methods()
    start_years = get_all_start_years()
    return {method: min(list(start_years[method].values())) for method in opts}

def ordered_list_methods_by_year():
    yrs = get_earliest_year()
    yr_list = list(yrs.values())
    yr_list.sort()
    lst_nested = [[method for method in yrs if yrs[method] == yr] for yr in yr_list] # Ordered list that is nested
    lst = []
    counter = 0
    for ent in lst_nested:
        if len(ent) > counter + 1:
            lst.append(ent[counter])
            counter += 1
        else:
            lst.append(ent[0])
            counter = 0
    return lst