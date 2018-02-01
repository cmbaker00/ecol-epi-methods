from citation_data import *
import matplotlib.pyplot as plt
import numpy as np
import ast
import seaborn as sns
import csv

def get_methods():
    return ['ethics','optim','costben','voi','adaptive','ibm','sdm','ensemble']

def full_meth_name(method):
    dict = {'ethics': 'Ethics', 'optim': 'Optimisation', 'costben': 'Cost-benefit', 'voi': 'Value of Information',
            'adaptive': 'Adaptive Management', 'ibm': 'Individual Based Model', 'sdm': 'Structured Decision-Making',
            'ensemble': 'Ensemble Models'}
    return dict[method]

def return_all_full_names():
    meths = get_methods()
    return [full_meth_name(method) for method in meths]

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
    if np.max(cum_citations) < 10:
        return None
    else:
        return t[cum_citations >= num][0]

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

def store_all_start_years():
    st_yrs = get_all_start_years()
    write_dict_to_file(st_yrs,'start_years_dictionary.txt')

def write_dict_to_file(dict, fname):
    file = open(fname, 'w')
    file.write(str(dict))
    file.close()

def read_start_years_from_file():
    return read_dict_from_file('start_years_dictionary.txt')

def read_dict_from_file(fname):
    file = open(fname, 'r')
    return ast.literal_eval(file.read())

def get_earliest_year():
    opts = get_methods()
    start_years = read_start_years_from_file()
    return {method: min(x for x in list(start_years[method].values()) if x is not None) for method in opts}

def min_ignore_none(lst):
    return min(x for x in lst if x is not None)
def max_ignore_none(lst):
    return max(x for x in lst if x is not None)

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

def custom_colours(col = 'all'):
    # colours = sns.color_palette("colorblind")
    colours = sns.color_palette("Set3",8)
    colours = sns.hls_palette(8, l=.5, s=.6)
    if col.isnumeric():
        return colours[col]
    elif col == 'all':
        return colours
    elif col == 'epi':
        return colours[0]
    elif col == 'cons':
        return colours[1]
    elif col == 'fish':
        return colours[2]
    else:
        return 'Unknown option'

def write_all_first_papers():
    for meth in get_methods():
        print_first_papers(meth)

def print_first_papers(meth):
    start_years = read_start_years_from_file()
    ff, fc, fe = file_names(meth)
    sy = start_years[meth]['fish']
    if sy == None:
        sy = 2018
    papers = get_paper_titles_before(sy,ff)
    # print(papers)
    save_paper_list_csv(ff, papers)
    sy = start_years[meth]['cons']
    if sy == None:
        sy = 2018
    papers = get_paper_titles_before(sy,fc)
    # print(papers)
    save_paper_list_csv(fc, papers)
    sy = start_years[meth]['epi']
    if sy == None:
        sy = 2018
    papers = get_paper_titles_before(sy,fe)
    # print(papers)
    save_paper_list_csv(fe, papers)
    # print(ff)

def save_paper_list_csv(fname, lst):
    ofile = open('../lit/{0}_firstpapers.csv'.format(fname), "w", newline="")
    writer = csv.writer(ofile)
    for title in lst:
        # print(title)
        writer.writerow([title])
    ofile.close()

def scatter_plot_F1(saveplot = False):
    start_years = read_start_years_from_file()
    meth_list = ordered_list_methods_by_year()
    height = 0
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for method in meth_list:
        height += 1
        ys = min_ignore_none(list(start_years[method].values()))
        ye = max_ignore_none(list(start_years[method].values()))
        gap = ye - ys
        plt.plot([ys,ye],[height,height],'k--', zorder = 0)
        plt.text(ys + gap/2 - 2 - .2*len(str(gap)), height + .2, '{0} Years'.format(gap))
        for fld in start_years['costben']:
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

    ax.yaxis.set_visible(False)
    if saveplot:
        plt.savefig('method_start_plot.png', bbox_inches='tight')
    plt.show()
