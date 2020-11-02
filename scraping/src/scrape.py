# Using 1 Self-service website and 1 Webadvisor site to test script
# Self-Service: https://selfsvc.blueridge.edu/Student/courses
# Webadvisor: https://online.blueridge.edu/WA/WebAdvisor?TOKENIDX=5857985298&SS=1&APP=ST&CONSTITUENCY=WBST

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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


###############################
# WedAdvisor
###############################

# get average number of pages per college
# get total online classes per college

# General process
# 1) go to site
# 2) click "Advanced Search" tab
# 3) click "Location" dropdown/select
# 4) Click "Internet Based Course" option



# interface either self service or webadvisor
# pass 0 for self service
# pass 1 for webadvisor
def get_school_data(url, abbr):
    driver.get(url)
    time.sleep(1)

    tab = driver.find_elements_by_class_name("esg-tab__link")[1]
    tab.click()
    time.sleep(1)

    term = Select(driver.find_elements_by_id("term-label-id")[1])
    term.select_by_value("2020FA")

    location = driver.find_element_by_css_selector("option[value='OL']")
    location.click()

    search_btn = driver.find_element_by_css_selector("input[value='Search']")
    search_btn.click()
    time.sleep(4)

    #####################
    # Extract Course and Section information from pages
    ######################
    last = get_total_pages() - 1
    for i in range(last):

        # click all buttons on page
        courselist = driver.find_element_by_id("course-resultul")
        click_course_bnts(courselist)


        # wait
        time.sleep(10)
        with open("output/ss/" + abbr + "/source" + page_num + ".html", "w") as file:
            file.write(driver.page_source)

        # parse page
        #esg-section--margin-top esg-section--border
        courses = courselist.find_elements_by_tag_name("li")

        # for each course
        for course in courses:
            sections = course.find_elements_by_css_selector('ul[data-bind="foreach: Sections"]')

        # for each section

        # write to file


        # if not last page -> next page
        if i != last:
            next_page()



get_school_data("https://sss.halifaxcc.edu/Student/Courses")
# get_school_data(
#     1, "https://online.blueridge.edu/WA/WebAdvisor?TOKENIDX=4390841124&SS=1&APP=ST&CONSTITUENCY=WBST")


# courses = <ul id=course-resultul" ... >
# -> course = <li>
# -> -> sections = <ul data-bind="foreach: Sections">
# -> -> -> section = <li class="search-nestedaccordionitem">
# -> -> -> ->


# Total pages
# total_pages = driver.find_element_by_css_selector("span[data-bind='text:TotalPages']").


def get_total_pages():
    return driver.find_element_by_css_selector("span[data-bind='text:TotalPages']").text

def next_page():
    next_page_btn = driver.find_element_by_id("course-results-next-page")
    next_page_btn.click()

def click_course_bnts(_courselist):
    collapsed = _courselist.find_elements_by_css_selector('button[class="esg-collapsible-group__toggle text-align-left"]')
    print("# of courses: ", len(collapsed))
    for button in collapsed:
        button.click()
    
