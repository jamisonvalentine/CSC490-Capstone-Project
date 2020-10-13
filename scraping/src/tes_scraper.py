from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import os

PATH = "../selenium/chromedriver.exe"
driver = webdriver.Chrome(PATH)

df = pd.read_excel("../../data/input/list_of_colleges.xlsx", index_col = 'School')

# import remaining
print(df.index)

# for each college in index
    # search college name in TES
    # click correponding link
    # change to 200 results
    # get total pages
    # for each page → get html
    # build eq table

# for each eq table
    # for each remaining
        # if in eq
            # print college & eq row

