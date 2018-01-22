from citation_data import *

def get_methods():
    return ['ethics','optim','costben','voi','adaptive','ibm','sdm','ensemble']

def file_names(method):
    ff = '{0}_fisheries'.format(method)
    fc = '{0}_cons'.format(method)
    fe = '{0}_epi'.format(method)
    return ff, fc, fe

