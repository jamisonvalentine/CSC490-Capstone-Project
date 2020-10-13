from bs4 import BeautifulSoup
import pandas as pd
import os


for root, dirs, files in os.walk("equivalencies/wtcc", topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        print(file_path)
    
        soup = BeautifulSoup(open(file_path), 'html.parser')

        table = soup.find("table", id="gdvCourseEQ")
        tbody = table.find("tbody")
        rows = tbody.find_all("tr")
        last_row = len(rows) - 2
        rows = rows[3: last_row]
        # print(rows[0])
        
        for row in rows:
            tmp = row.find_all("td")
            caa = tmp[1]
            uncg = tmp[2]
            print(caa.get_text().strip())
            print(uncg.get_text().strip())
            print("////////////////////")