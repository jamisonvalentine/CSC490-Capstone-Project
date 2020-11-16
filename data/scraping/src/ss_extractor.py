from bs4 import BeautifulSoup
import pandas as pd
import os
import sys
import re

def rmws(x):
    return s.sub(" ", x)

def format_days(x):
   x = x.replace("/", ", ")
   x = x.replace('Th,', "Thursday,")
   x = x.replace("T, ", "Tuesday,")
   x = x.replace("M,", "Monday,")
   x = x.replace("W,", "Wednesday")
   
   x = x.replace("M ", "Monday")
   x = x.replace("T ", "Tuesday")
   x = x.replace("W ", "Wednesday")
   x = x.replace("Th ", "Thursday")
   x = x.replace("F ", "Friday")
   return x



ss_courses = pd.DataFrame(columns=['college', 'section', 'credits', 'instructor', 'dates', 'location'])

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
            title = m.group(1)[8:]
            credit = m.group(2)        


            section_blocks = list(course.select("table.esg-table.esg-table--no-mobile.esg-section--margin-bottom.search-sectiontable"))
            for block in section_blocks:
                section = block.select('a')[0].get_text()

                rows = list(block.select("td.search-sectiondaystime"))
                n = len(block.select("tr.search-sectionrow")) - 1
                # loc = list(block.select("td.search-sectionlocations"))

                # s = re.compile("\s+")
  
                # if n > 0:
                #     dates = list(map(lambda x: rmws(x.get_text()), dates))
                #     loc = list(map(lambda x: rmws(x.get_text()), loc))                    
                        
                #     str1 = ""
                #     for i in range(n):
                #         str1 += dates[i] + loc[i]
                    
                #     dates = str1
                # else:
                #     dates = "TBD"
                #     loc = "TBD"

                if n > 0:
                    info = ""
                    tmp = {"data-bind": "text: $data.DatesDisplay(), attr: { id: 'section-'+$parent.Section.Id()+'-meeting-dates-'+$index()}"}
                    dates = list(block.find_all("span", attrs = tmp))

                    tmp = {"data-bind": "text: $data.InstructionalMethodDisplay(), attr: { id: 'section-'+$parent.Section.Id+'-meeting-instructional-method-'+$index() }"}
                    types_ = block.find_all("span", attrs = tmp)

                    tmp = {"data-bind": "text: $data.DaysOfWeekDisplay() + ' ', attr: { id: 'section-'+$parent.Section.Id()+'-meeting-days-'+$index()}"}
                    days = block.find_all("span", attrs = tmp)

                    tmp = {"data-bind": "text: $data.StartTimeDisplay(), attr: { id: 'section-'+$parent.Section.Id()+'-meeting-times-start-'+$index()}"}
                    time_starts = block.find_all("span", attrs = tmp)

                    tmp = {"data-bind": "text: $data.EndTimeDisplay, attr: { id: 'section-'+$parent.Section.Id()+'-meeting-times-end-'+$index()}"}
                    time_ends = block.find_all("span", attrs = tmp)

                    tmp = {"data-bind": "text: $parent.Section.LocationDisplay(), visible: !isNullOrEmpty($parent.Section.LocationDisplay()), attr: { id: 'section-'+$parent.Section.Id()+'-meeting-location-'+$index() }"}
                    locations = block.find_all("span", attrs = tmp)

                    tmp = {"data-bind": "text: $data.BuildingDisplay(), visible: !isNullOrEmpty($data.BuildingDisplay())"}
                    buildings = block.find_all("span", attrs = tmp)

                    tmp = {"data-bind": "text: ' ' + $data.RoomDisplay(), visible: !isNullOrEmpty($data.RoomDisplay())"}
                    rooms = block.find_all("span", attrs = tmp)

                    for i in range(n):

                        date = dates[i].get_text().replace(" ", "")
                        type_ = types_[i].get_text()
                        building = buildings[i].get_text()
                        room = rooms[i].get_text()

    
                        if "Online" in type_ or "Internet" in building or "line" in room.lower():
                            day = "Days to be Announced"
                            time_start = "Times to be Announced"
                            time_end = ""
                            online = True
                        else:
                            day = format_days(days[i].get_text())
                            time_start = time_starts[i].get_text()
                            time_end = time_ends[i].get_text()
                            online = False

                        info_str = date + " " + type_ + " " + day + " " + time_start + ("" if online else " - " + time_end + ", ") + building + ", Room" + room
                        print(info_str)

                instructor_tmp = block.select("td.search-sectioninstructors")

                try:
                    instructor = instructor_tmp[0].select("div")[0].select("span")[0].get_text()
                except: instructor = "TBD"

                row = {'college': college, "section": section + " " + title, "credits": credit, "instructor": instructor, "dates": info_str, "location": building}            

                # print(row)
                print(section, title)
                ss_courses = ss_courses.append(row, ignore_index=True)

ss_courses.to_csv("ss_courses_sp2021.csv", index=False)
ss_courses.to_csv("../../output/ss_courses_sp2021.csv", index=False)
print(len(ss_courses))
