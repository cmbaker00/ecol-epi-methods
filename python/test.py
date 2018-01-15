import csv
import numpy as np
import matplotlib.pyplot as plt
# import sys
#
# sys.path.insert(0,'../lit')

def get_citations_by_year(file):
    file = csv.reader(open('../lit/{0}.csv'.format(file), newline=''), delimiter=',')

    flag = False
    for row in file:
        # print(row)
        if row[0] == 'Title':
            ys = row.index('1900')
            ye = row.index('2018')
            flag = True
            flag_first = True
        elif flag:
            y_data = np.array(row[ys:ye]).astype(np.float)
            if flag_first:
                citations = np.array(y_data)
                flag_first = False
            else:
                citations = np.vstack([citations, y_data])
    t = np.arange(1900,2018)
    return t, np.sum(citations,0)
t, citations = get_citations_by_year('voi_epi')
plt.plot(t,citations)
plt.show()