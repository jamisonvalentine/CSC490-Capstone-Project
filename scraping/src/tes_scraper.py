from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time


PATH = "../../selenium/chromedriver.exe"
driver = webdriver.Chrome(PATH)



# ref for search box

# Get list of schools
df = pd.read_excel("../../data/input/list_of_colleges.xlsx", index_col = 'School')

# import remaining


# test workflow for one school
for index in df.index:
    print(index)

    # Navigate to TES website
    driver.get("https://tes.collegesource.com/publicview/TES_publicview01.aspx?rid=200AB5D2-A95C-4895-9836-300D49A73FD1&aid=CFC487EB-2770-451B-8B5D-A20C08DB6323")    
    search_box = driver.find_element_by_id("tbxSearchTransferCollege")
    search_box.send_keys(index, Keys.ENTER)

    # if link returned, click the first one
    link = driver.find_element_by_id("gdvInstWithEQ_btnCreditFromInstName_0")

    try:
        link.click()
    except:
        print('No link found for ', index)
        continue

    # click search button
    search_btn = driver.find_element_by_id("btnSearchEQ")
    search_btn.click()
    time.sleep(2)

    records = driver.find_element_by_id("ddlRecordsPerPage")
    records.click()
    _200 = records.find_elements_by_tag_name("option")[3]
    _200.click()

    search_btn2 = driver.find_element_by_id("btnCourseEQSearch")
    search_btn2.click()
    time.sleep(6)

    # get pages
    pages = driver.find_element_by_css_selector("tr.pagination-tes")
    pg_nums = pages.find_elements_by_tag_name("a")
    last = int(pg_nums[len(pg_nums) - 1].text)
    
    for i in range(last):
        pages = driver.find_element_by_css_selector("tr.pagination-tes")
        pg_nums = pages.find_elements_by_tag_name("a")

        print('current page: ', i+1)
        print('last: ', last)

        # get html and save

        html = driver.page_source
        print('source scraped')

        dir_ = "../output/tes/" + index

        if not os.path.isdir(dir_):
            os.makedirs(dir_)

        with open(dir_ + "/source_" + str(i) + ".html", "wb") as file:
            file.write(html.encode('utf-8'))
        
        print('written')
        if i != last-1:
            time.sleep(2)
            pg_nums[i].click()
            time.sleep(5)        

        # if not last → click next







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

