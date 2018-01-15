import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'/python')
from citation_data import *

opts = ['ethics','optim','costben','voi','adaptive','ibm','sdm','ensemble']

method = opts[4]
ff = '{0}_fisheries'.format(method)
fc = '{0}_cons'.format(method)
fe = '{0}_epi'.format(method)

t, citations = get_citations_by_year('voi_epi')
plt.plot(t,citations)
plt.show()

