from bs4 import BeautifulSoup
import pandas as pd
import os

eq = pd.DataFrame(columns = ['caa_id', 'caa_title', 'uncg_id', 'uncg_title'])

for root, dirs, files in os.walk("../output/tes", topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        print(name)
        soup = BeautifulSoup(open(file_path), 'html.parser')

        table = soup.find("table", id="gdvCourseEQ")
        tbody = table.find("tbody")
        rows = tbody.find_all("tr")
        last_row = len(rows) - 2
        rows = rows[3: last_row]
        
        for row in rows:
            tmp = row.find_all("td")
            caa = tmp[1].get_text().strip()
            caa_id = caa[:7]
            caa_title = caa[8:]
            uncg = tmp[2].get_text().strip()
            uncg_id = uncg[:7]
            uncg_title = uncg[8:]
            entry = {'caa_id': caa_id, 'caa_title': caa_title, 'uncg_id': uncg_id, 'uncg_title': uncg_title}
            eq = eq.append(entry, ignore_index=True)

eq.set_index('caa_id', drop=True, inplace=True)
eq.to_excel("../output/equivalencies2.xlsx")
