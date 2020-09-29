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
    return driver.find_elements_by_css_select("//*[contains(text(), 'My Button')]")

def next_page():
    next_btn = driver.find_elements_by_css_select('input[value="NEXT"]')
    next_btn.click()

def get_school_data(dir_name, url):
    driver.get(url)
    time.sleep(1)

    tab = driver.find_elements_by_xpath("//span[contains(text(), 'Search for Sections')]")
    tab.click()
    time.sleep(1)

    term = Select(driver.find_element_by_id("VAR1"))
    term.select_by_value("2020FA")

    search_btn = driver.find_element_by_css_selector("input[value='SUBMIT']")
    search_btn.click()
    time.sleep(10)

    #####################
    # Extract HTML
    ######################
    last = int(get_total_pages())
    print('total pages: ', last)
    for i in range(1, last+1):
        print('current page: ', i)

        # wait
        time.sleep(3)
        html = driver.page_source

        dir = "output/ww/" + dir_name

        if not os.path.isdir(dir):
            os.makedirs(dir)

        with open(dir + "/source_" + str(i) + ".html", "wb") as file:
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



