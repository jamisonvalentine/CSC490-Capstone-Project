# Using 1 Self-service website and 1 Webadvisor site to test script
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
# 4) click "Location" dropdown/select
# 5) Click "Internet Based /';Course" option
#	for each page:
#		for each course:


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



# interface either self service or webadvisor
# pass 0 for self service
# pass 1 for webadvisor
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

    online_filter = driver.find_element_by_css_selector('label[for="' + filt + '"]')
    online_filter.click()
    time.sleep(2)

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
                time.sleep(2)

        # parse page
        #esg-section--margin-top esg-section--border
        # courses = courselist.find_elements_by_tag_name("li")

        # for each course
        # for course in courses:
        #     sections = course.find_elements_by_css_selector('ul[data-bind="foreach: Sections"]')

        # for each section

        # write to file


        # if not last page -> next page



# courses = <ul id=course-resultul" ... >
# -> course = <li>
# -> -> sections = <ul data-bind="foreach: Sections">
# -> -> -> section = <li class="search-nestedaccordionitem">
# -> -> -> ->


# Total pages
# total_pages = driver.find_element_by_css_selector("span[data-bind='text:TotalPages']").



    
