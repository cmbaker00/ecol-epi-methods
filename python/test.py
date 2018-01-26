import numpy as np
import matplotlib.pyplot as plt
import sys
from citation_data import *
from nrm_functions import *

opts = get_methods()

start_years = get_all_start_years()
meth_list = ordered_list_methods_by_year()
height = 0
# for method in meth_list:
#     height += 1
#     for fld in start_years['costben']:
#         # continue
#         print(cols[fld])
#         plt.scatter(start_years[method][fld], height, s = 100, c = custom_colours(fld))
# plt.plot(list(start_years['ethics'].values()))
# plt.close()
fld = 'epi'
method = 'ensemble'

ff, fc, fe = file_names(method)
titles = get_paper_titles_before(start_years[method][fld], fe)