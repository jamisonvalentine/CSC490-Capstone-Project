# Using 1 Self-service website and 1 Webadvisor site to test script
# Self-Service: https://selfsvc.blueridge.edu/Student/courses
# Webadvisor: https://online.blueridge.edu/WA/WebAdvisor?TOKENIDX=5857985298&SS=1&APP=ST&CONSTITUENCY=WBST

from bs4 import bs
import requests

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
def get_school_data(interface, url):
