"""
updates the page with the research work of the faculty
"""

import json
import requests
from bs4 import BeautifulSoup

data = json.loads(open("./json_data/faculty-info.json").read())
for x in data:

    for y in range(len(data[x])):
        try:
            url = "./pages/" + x + "/" + data[x][y]["url"].split("/")[-1]
            page = open(url, "r", encoding="utf-8", errors="replace").read()
            soup = BeautifulSoup(page, 'html.parser')
            div = soup.find("div", {"id": "research"})
            div = div.find("div")
            data[x][y]["research"] = eval(div["data-attr-research-json"])
        except:
            print("Error in ", x, y)
            continue

file = open("./json_data/research-faculty-info.json", "w")
file.write(json.dumps(data))

# open("test.txt", "w").write(soup.prettify())