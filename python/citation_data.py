import csv
import numpy as np

def get_citations_by_year(file):
    file = csv.reader(open('../lit/{0}.csv'.format(file), newline=''), delimiter=',')

    flag = False
    yrs = []
    for row in file:
        # print(row)
        if row[0] == 'Title':
            ys = row.index('1900')
            ye = row.index('2018')
            flag = True
            flag_first = True
        elif flag:
            y_data = np.array(row[ys:ye]).astype(np.float)
            yrs.append(row[7])
            if flag_first:
                citations = np.array(y_data)
                flag_first = False
            else:
                citations = np.vstack([citations, y_data])
    t = np.arange(1900,2018)
    return t, np.sum(citations,0), np.array(create_frequency(t, [float(t) for t in yrs]))

def create_frequency(years, data):
    return [sum(data == t) for t in years]