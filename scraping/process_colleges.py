import pandas as pd
from scrape2 import *

colleges = pd.read_excel("../data/list_of_colleges.xlsx", index_col="School")
ss = colleges.loc[colleges["ss_url"].notna()]
print(len(ss))

print(ss['ss_url'])

for index, row in ss[:3].iterrows():
    print('index: ', index)
    print('url: ', row['ss_url'])
    get_school_data(index, row['ss_url'])
    colleges[index]["scrape_complete"] = 'x'

    


