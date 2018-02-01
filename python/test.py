import numpy as np
import matplotlib.pyplot as plt
import sys
from citation_data import *
from nrm_functions import *

get_start_years = False

opts = get_methods()
if get_start_years:
    store_all_start_years()
start_years = read_start_years_from_file()
meth_list = ordered_list_methods_by_year()
height = 0
fig = plt.figure()
ax = fig.add_subplot(111)
for method in meth_list:
    height += 1
    ys = min_ignore_none(list(start_years[method].values()))
    ye = max_ignore_none(list(start_years[method].values()))
    plt.plot([ys,ye],[height,height],'k--', zorder = 0)
    for fld in start_years['costben']:
        # continue
        plt.scatter(start_years[method][fld], height, s = 100, c = custom_colours(fld))

yr_start = 2010
text_offset = .15
st_height = 1.25
heigh_offset = .75
legend_dot_size = 200

plt.scatter(yr_start - 1,st_height + heigh_offset*2, s = legend_dot_size, c = custom_colours('epi'))
ax.text(yr_start,st_height + heigh_offset*2 - text_offset,'Epidemiology')
plt.scatter(yr_start - 1,st_height + heigh_offset, s = legend_dot_size, c = custom_colours('cons'))
ax.text(yr_start,st_height + heigh_offset - text_offset,'Conservation')
plt.scatter(yr_start - 1,st_height, s = legend_dot_size, c = custom_colours('fish'))
ax.text(yr_start,st_height - text_offset,'Fisheries')
yticklabels = return_all_full_names()
yticklabels.insert(0,'')
yticklabels = [st.title() for st in yticklabels]

ax.set_yticklabels('')

yticklabels.pop(0)
hgt = 1
for ytl in yticklabels:
    sty = min_ignore_none(list(start_years[meth_list[hgt-1]].values()))
    h_offset = 0.4 + .65*len(ytl)
    if ytl == 'Adaptive Management':
        h_offset += 1
    ax.text(sty - h_offset,hgt - text_offset/2,ytl)
    hgt += 1


# plt.yticks(rotation='vertical')
fld = 'epi'
method = 'ensemble'

ff, fc, fe = file_names(method)
titles = get_paper_titles_before(start_years[method][fld], fe)

plt.show()
