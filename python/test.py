import numpy as np
import matplotlib.pyplot as plt
import sys
from citation_data import *
from nrm_functions import *

opts = get_methods()

start_years = get_all_start_years()
meth_list = ordered_list_methods_by_year()
height = 0
fig = plt.figure()
ax = fig.add_subplot(111)
for method in meth_list:
    height += 1
    for fld in start_years['costben']:
        # continue
        plt.scatter(start_years[method][fld], height, s = 100, c = custom_colours(fld))

yr_start = 1983
text_offset = .15
plt.scatter(yr_start - 1,8, s = 100, c = custom_colours('epi'))
ax.text(yr_start,8 - text_offset,'Epidemiology')
plt.scatter(yr_start - 1,7, s = 100, c = custom_colours('cons'))
ax.text(yr_start,7 - text_offset,'Conservation')
plt.scatter(yr_start - 1,6, s = 100, c = custom_colours('fish'))
ax.text(yr_start,6 - text_offset,'Fisheries')
yticklabels = return_all_full_names()
yticklabels.insert(0,'')
yticklabels = [st.title() for st in yticklabels]

ax.set_yticklabels(yticklabels)

# plt.close()
fld = 'epi'
method = 'ensemble'

ff, fc, fe = file_names(method)
titles = get_paper_titles_before(start_years[method][fld], fe)