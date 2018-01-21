import numpy as np
import matplotlib.pyplot as plt
import sys
pth = sys.path
pth.append(pth[-1] + '/python')
sys.path = pth

# sys.path.insert(0,'/python')
from citation_data import *

opts = ['ethics','optim','costben','voi','adaptive','ibm','sdm','ensemble']

method = opts[4]
ff = '{0}_fisheries'.format(method)
fc = '{0}_cons'.format(method)
fe = '{0}_epi'.format(method)

t, citations = get_citations_by_year(ff)
trange = t <= 2015
plt.plot(t[trange],citations[trange])
plt.show()

