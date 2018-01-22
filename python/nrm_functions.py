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
