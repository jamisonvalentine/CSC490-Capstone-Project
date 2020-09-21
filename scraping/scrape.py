# Using 1 Self-service website and 1 Webadvisor site to test script
# Self-Service: https://selfsvc.blueridge.edu/Student/courses
# Webadvisor: https://online.blueridge.edu/WA/WebAdvisor?TOKENIDX=5857985298&SS=1&APP=ST&CONSTITUENCY=WBST

from bs4 import BeautifulSoup as bs
from selenium import webdriver
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
# 3) click "Location" dropdown/select
# 4) Click "Internet Based /';Course" option
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
#


# interface either self service or webadvisor
# pass 0 for self service
# pass 1 for webadvisor
def get_school_data(interface, url):
    driver.get(url)
    time.sleep(3)
    print(driver.title)
    tab = driver.find_elements_by_class_name("esg-tab__link")[1]
    tab.click()
    time.sleep(1)
    selects = driver.find_elements_by_id("term-label-id")

    for index, val in enumerate(selects):
        print('# ' + str(index) + ": " + val.get_attribute("id"))

        selects[1].click()


# # links = driver.find_elements_by_tag_name("a")
# # for index, val in enumerate(links):
# #     print('# ' + str(index) + ": " + val.get_attribute("class"))

# lists = driver.find_elements_by_tag_name("li")
# for index, val in enumerate(lists):
#     print('# ' + str(index) + ": " + val.get_attribute("class"))

# html = driver.page_source
# soup = bs(html, 'lxml')
# link = soup.findAll("a")
# print(len(link))

# tab = driver.find_elements_by_class_name("esg-tab__link")
# print(tab)
# print(driver.page_source)
# driver.quit()
get_school_data(0, "https://sss.halifaxcc.edu/Student/Courses")
# get_school_data(
#     1, "https://online.blueridge.edu/WA/WebAdvisor?TOKENIDX=4390841124&SS=1&APP=ST&CONSTITUENCY=WBST")
