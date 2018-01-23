import numpy as np
import matplotlib.pyplot as plt
import sys
from citation_data import *
from nrm_functions import *

opts = get_methods()

start_years = get_all_start_years()
meth_list = ordered_list_methods_by_year()
plt.plot(list(start_years['ethics'].values()))
plt.close()