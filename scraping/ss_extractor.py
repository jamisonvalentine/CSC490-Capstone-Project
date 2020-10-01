from bs4 import BeautifulSoup
import pandas as pd
import os


courses = pd.DataFrame(columns=['college', 'section', 'seats', 'instructor'])

for root, dirs, files in os.walk("output/ss", topdown=False):
#    print(len(files))
    parts = root.split("\\")
    college = parts[1] if len(parts) > 1 else ""
    print(college)
    for name in files:
        file_path = os.path.join(root, name)
    
        soup = BeautifulSoup(open(file_path), 'html.parser')
        # section_blocks = list(soup.select("li.search-nestedaccordionitem"))

        blocks = list(soup.select("table.esg-table.esg-table--no-mobile.esg-section--margin-bottom.search-sectiontable"))
        # print(list(blocks[0].tbody.contents[3]))
        for b in blocks:
            section = b.select('a')[0].get_text()
            seats = b.select("span.search-seatsavailabletext")[0].get_text()
            dates = b.select("td.search-sectiondaystime")[0].select("div")[1].span.get_text()
            i = b.select("td.search-sectioninstructors")
            instructor = i[0].select("div")[0].select("span")[0].get_text()
            row = college + "\t" + section + "\t" + seats + "\t" + dates + "\t" + instructor
            print(row)
            row = {'college': college, "section": section, "seats": seats, "instructor":instructor}
            courses = courses.append(row, ignore_index=True)


courses.to_csv("courses.csv")
print('# of courses: ', len(courses))
