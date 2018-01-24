import numpy as np
import matplotlib.pyplot as plt
import sys
from citation_data import *
from nrm_functions import *

opts = get_methods()

start_years = get_all_start_years()
meth_list = ordered_list_methods_by_year()
cols = {'epi':.4, 'cons': .2, 'fish': .9}
height = 0
for method in meth_list:
    height += 1
    for fld in start_years['costben']:
        # continue
        print(cols[fld])
        plt.scatter(start_years[method][fld], height, s = 100, c = custom_colours(fld))
        oops this is a mistake
# plt.plot(list(start_years['ethics'].values()))
# plt.close()