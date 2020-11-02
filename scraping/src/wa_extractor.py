from bs4 import BeautifulSoup
import pandas as pd
import os

courses = pd.DataFrame(
    columns=['college', 'section', 'credits', 'instructor', 'dates', 'location'])

for root, dirs, files in os.walk("output/wa", topdown=False):
    #    print(len(files))
    parts = root.split("\\")
    college = parts[1] if len(parts) > 1 else ""
    print(college)
    for name in files:
        file_path = os.path.join(root, name)

        soup = BeautifulSoup(open(file_path), 'html.parser')

        try:
            table = soup.find(summary="Sections")
            body = table.tbody
        except:
            table = soup.select("table.noSpacing")[0]
            body = table.tbody            
        a = {}
        rows = body.find_all("tr", recursive=False)
        header = rows[1]
        hcells = header.find_all("th")[:]
        start_row=2
        alt_table = False

        if len(hcells) < 1:
            header = rows[0]
            hcells = header.find_all("div", class_="sortButton")
            alt_table = True
            start_row = 1

        for i, h in enumerate(hcells):
            h = h.get_text()
            if "Title" in h:
                a["title"] = i
            if "Credit" in h:
                a["credits"] = i
            if "Location" in h:
                a["location"] = i
            if "Faculty" in h:
                a["instructor"] = i
            if "Available" in h:
                a["seats"] = i
            if "Meeting" in h:
                a["dates"] = i

        for row in rows[start_row:]:

            cells = row.find_all("td")
            if alt_table: cells.pop(1)
            # print('cells: ', len(cells))
            section = cells[a["title"]].get_text().strip()
            loc = cells[a["location"]].get_text().strip()
            dates = cells[a["dates"]].get_text().strip()
            instructor = cells[a["instructor"]].get_text().strip()
            seats = cells[a["seats"]].get_text().strip()
            credit = cells[a["credits"]].get_text().strip()
            print(college + " " + section + " " + loc + " " + dates + " " + instructor + " " + seats + " " + credit )
            entry = {'college': college, "section": section,
                    "credits": credit, "instructor": instructor, "dates": dates, "location": loc}
            courses = courses.append(entry, ignore_index=True)

# courses.to_csv("wa_courses.csv")
print('# of courses: ', len(courses))
