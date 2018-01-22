import numpy as np
import matplotlib.pyplot as plt
import sys
# pth = sys.path
# pth.append(pth[-1] + '/python')
# sys.path = pth

# sys.path.insert(0,'/python')
from citation_data import *
from nrm_functions import *

opts = get_methods()

method = opts[4]
ff, fc, fe = file_names(method)

t, citations = get_citations_by_year(ff)
trange = (t <= 2015) & (t > 1950)
plt.plot(t[trange],citations[trange])
plt.show()

