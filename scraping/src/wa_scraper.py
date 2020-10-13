from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time

PATH = "../selenium/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# visit page
# click span w/ Search for Sections text
# select option value 2020FA
# select appropriate option value
# click SUBMIT
# get total pages (find by text: driver.find_elements_by_xpath("//*[contains(text(), 'My Button')]"))
# save page source
# if not last page, click next button
# → if not standard input button, then (find by text: driver.find_elements_by_xpath("//*[contains(text(), 'NEXT')]"))


def get_total_pages():
    box = driver.find_element_by_xpath("//*[contains(text(), 'Page 1')]")
    string = box.get_attribute("innerText").split(" ")
    return string[3]

def next_page():
    try:
        next_btn = driver.find_element_by_css_selector('input[value="NEXT"]')
    except:
        next_btn = driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
    next_btn.click()

def get_wa_school_data(dir_name, url, filt):
    driver.get(url)
    time.sleep(1)

    tab = driver.find_element_by_xpath("//span[contains(text(), 'Search for Sections')]")
    tab.click()
    time.sleep(1)

    term = Select(driver.find_element_by_id("VAR1"))

    try:
        term.select_by_value("2020FA")
    except:
        term.select_by_value("20/FA")


    try:
        # loc = driver.find_element_by_css_selector("option[value='" + filt + "']")
        loc = Select(driver.find_element_by_id("VAR21"))
        loc.select_by_value("CU")
    except:
        print("no CU value")
    

    search_btn = driver.find_element_by_css_selector("input[value='SUBMIT']")
    search_btn.click()
    time.sleep(30)

    ####################
    ## Extract HTML
    #####################
    last = int(get_total_pages())
    print('total pages: ', last)
    for i in range(1, last+1):
        print('current page: ', i)

        # wait
        time.sleep(3)
        html = driver.page_source

        dir_ = "output/wa/" + dir_name

        if not os.path.isdir(dir_):
            os.makedirs(dir_)

        with open(dir_ + "/source_" + str(i) + ".html", "wb") as file:
            file.write(html.encode('utf-8'))

            if i != last:
                next_page()
                time.sleep(1)












# parse page
#esg-section--margin-top esg-section--border
# courses = courselist.find_elements_by_tag_name("li")

# for each course
# for course in courses:
#     sections = course.find_elements_by_css_selector('ul[data-bind="foreach: Sections"]')

# for each section



