from citation_data import *
from nrm_functions import *

re_read_data = True
if re_read_data:
    store_all_start_years()
    write_all_first_papers()
    save_all_method_topic_searches()

scatter_plot_F1()
