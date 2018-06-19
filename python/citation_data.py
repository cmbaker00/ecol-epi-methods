import csv
import numpy as np
import os.path
import pandas as pd
import os
def get_citations_by_year(filename):
    ignore = list_ignore(filename)
    if os.path.isfile('../lit/{0}.csv'.format(filename)):
        pass
    elif os.path.isfile('../lit/{0}.xls'.format(filename)):
        data_xls = pd.read_excel('../lit/{0}.xls'.format(filename), 'savedrecs', index_col=None)
        data_xls.to_csv('../lit/{0}.csv'.format(filename), encoding='utf-8', index=False)
    else:
        raise Exception('File does not exist: {0}.csv or {0}.xls'.format(filename))

    file = csv.reader(open('../lit/{0}.csv'.format(filename), newline=''), delimiter=',')

    flag = False
    yrs = []
    for row in file:
        # print(row)
        if row[0] == 'Title':
            try:
                ys = row.index('1900')
                ye = row.index('2018')
            except:
                ys = row.index('1900.0')
                ye = row.index('2018.0')

            flag = True
            flag_first = True
        elif flag and row[0] not in ignore:
            y_data = np.array(row[ys:ye]).astype(np.float)
            yr = row[7]
            if yr[0].isalpha():
                yr = row[8]
            yrs.append(yr)
            if flag_first:
                citations = np.array(y_data)
                flag_first = False
            else:
                citations = np.vstack([citations, y_data])
    t = np.arange(1900,2018)
    return t, np.sum(citations,0), np.array(create_frequency(t, [float(t) for t in yrs]))

def create_frequency(years, data):
    return [sum(data == t) for t in years]

def get_paper_titles_before(year, filename):
    file = csv.reader(open('../lit/{0}.csv'.format(filename), newline=''), delimiter=',')
    titles = []
    authors = []
    years = []
    flag = False
    for row in file:
        # print(row)
        if row[0] == 'Title':
            flag = True
            flag_first = True
        elif flag:
            yr = row[7]
            if yr[0].isalpha():
                yr = row[8]
            yr = float(yr)
            if yr <= year:
                titles.append(row[0])
                authors.append(row[1])
                years.append(row[7])
    return titles, authors, years

def list_ignore(filename):
    fpath = '../lit/{0}_ignore.csv'.format(filename)
    if os.path.isfile(fpath):
        file = csv.reader(open(fpath, newline=''), delimiter=',')
        lst = []
        for row in file:
            if isinstance(row, list):
                title = row[0]
            elif isinstance(row, str):
                title = row
            if len(title) > 0:
                lst.append(title)
    else:
        lst = []
    return lst
