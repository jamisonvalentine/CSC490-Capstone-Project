# Examples of different interfaces
# Self-Service: https://selfsvc.blueridge.edu/Student/courses
# Webadvisor: https://online.blueridge.edu/WA/WebAdvisor?TOKENIDX=5857985298&SS=1&APP=ST&CONSTITUENCY=WBST

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time

PATH = "../selenium/chromedriver.exe"
driver = webdriver.Chrome(PATH)

###############################
# Self Service
###############################

# get average number of pages per college
# get total online classes per college

# General process
# 1) go to site
# 2) click "Advanced Search" tab
# 3) click "Term" dropdown/select
# 4) select Fall 2020 option
# 5) click Search
# 6) get total pages
# 7) click all collapsible buttons
# 8) save html
# 9) click next page
# 10) repeat for all pages

def get_total_pages():
    return driver.find_element_by_css_selector("span[data-bind='text:TotalPages']").text

def next_page():
    next_page_btn = driver.find_element_by_id("course-results-next-page")
    next_page_btn.click()

def click_course_bnts(_courselist):
    collapsed = _courselist.find_elements_by_css_selector('button[class="esg-collapsible-group__toggle text-align-left"]')
    time.sleep(2)
    # print("# of courses: ", len(collapsed))
    for button in collapsed:
        button.click()

def click_term_btns(_courselist):
    collapsed = _courselist.find_elements_by_css_selector(
        "div[class='esg-collapsible-group__body esg-is-open']")
    time.sleep(2)
    for button in collapsed:
        button.click()


def get_ss_school_data(dir_name, url, filt):
    driver.get(url)
    time.sleep(1)

    tab = driver.find_elements_by_class_name("esg-tab__link")[1]
    tab.click()
    time.sleep(1)

    term = Select(driver.find_elements_by_id("term-label-id")[1])
    term.select_by_value("2020FA")

    search_btn = driver.find_element_by_css_selector("input[value='Search']")
    search_btn.click()
    time.sleep(10)

    # filters = driver.find_elements_by_tag_name("input")
    # for filt in filters:
    #     print("id: ", filt.get_attribute("id"))

    # online_filter = driver.find_element_by_css_selector('label[for="' + filt + '"]')
    # online_filter.click()
    # time.sleep(5)

    #####################
    # Extract Course and Section information from pages
    ######################
    last = int(get_total_pages())
    print('total pages: ', last)
    for i in range(1,last+1):
        print('current page: ', i)
        # click all buttons on page
        courselist = driver.find_element_by_id("course-resultul")
        time.sleep(2)
        click_course_bnts(courselist)

        if url == "https://selfserve.waketech.edu/Student/Courses":
            click_term_btns(courselist)


        # wait
        time.sleep(8)
        html = driver.page_source

        dir_ = "output/ss/" + dir_name

        if not os.path.isdir(dir_):
            os.makedirs(dir_)

        with open(dir_ + "/source_" + str(i) + ".html", "wb") as file:
            file.write(html.encode('utf-8'))
            if i != last:
                next_page()
                time.sleep(5)





    
