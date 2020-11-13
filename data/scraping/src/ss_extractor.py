from bs4 import BeautifulSoup
import pandas as pd
import os
import sys
import re

def rmws(x):
    return s.sub(" ", x)

ss_courses = pd.DataFrame(columns=['college', 'section', 'credits', 'instructor', 'meeting_info', 'location'])

for root, dirs, files in os.walk("../input/2021/ss", topdown=False):
#    print(len(files))
    parts = root.split("\\")
    college = parts[1] if len(parts) > 1 else ""
    print(college)
    for name in files:
        file_path = os.path.join(root, name)
    
        soup = BeautifulSoup(open(file_path), 'html.parser')
        # section_blocks = list(soup.select("li.search-nestedaccordionitem"))

        courselist = soup.find(id="course-resultul")
        courses = courselist.find_all("li", recursive=False)


        for course in courses:

            title = course.find("span", attrs = {"data-bind": re.compile("Ceus")}).get_text()

            m = re.search("(.*) \((\d).*\)", title)
            title = m.group(1)
            credit = m.group(2)        


            blocks = list(course.select("table.esg-table.esg-table--no-mobile.esg-section--margin-bottom.search-sectiontable"))
            for b in blocks:
                section = b.select('a')[0].get_text()

                dates = list(b.select("td.search-sectiondaystime"))
                loc = list(b.select("td.search-sectionlocations"))

                s = re.compile("\s+")
  
                if len(dates) > 0:
                    dates = list(map(lambda x: rmws(x.get_text()), dates))
                    loc = list(map(lambda x: rmws(x.get_text()), loc))                    
                        
                    str1 = ""
                    for i in range(len(dates)):
                        str1 += dates[i] + loc[i]
                    
                    dates = str1
                else:
                    dates = "TBD"
                    loc = "TBD"



                instructor_tmp = b.select("td.search-sectioninstructors")

                try:
                    instructor = instructor_tmp[0].select("div")[0].select("span")[0].get_text()
                except: instructor = "TBD"



                row = {'college': college, "section": section + " " + title, "credits": credit, "instructor": instructor, "meeting_info": dates, "location": loc}            

                print(row)
                ss_courses = ss_courses.append(row, ignore_index=True)

ss_courses.to_csv("ss_courses_sp2021.csv", index=False)
ss_courses.to_csv("../../output/ss_courses_sp2021.csv", index=False)
print(len(ss_courses))
