import pandas as pd
from ss_scraper import *
# from wa_scraper import *

# wa_file = "../data/wa_interface.xlsx"
# wa = pd.read_excel(wa_file, index_col="School")
# for index, row in wa.iterrows():

#     if row['scrape_complete'] != 'x':
#         try:
#             print('index: ', index)
#             get_wa_school_data(index, row['wa_url'], row['loc_value'])
#             wa.loc[index, "scrape_complete"] = 'x'
#         except: 
#             print('could not extract for ', index)

# wa.to_excel(wa_file)


ss_file = "../data/ss_interface.xlsx"
ss = pd.read_excel(ss_file, index_col="School")
for index, row in ss.iterrows():
    if row['scrape_complete'] != 'x':
        try:
            print('index: ', index)
            get_ss_school_data(index, row['ss_url'], row['online_filter_id'])
            ss.loc[index, "scrape_complete"] = 'x'
        except ValueError:
            driver.close()
            print('could not extract for ', index)
            print(ValueError + "\n\n")
driver.close()

ss.to_excel(ss_file)


    


