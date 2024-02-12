"""
updates the page with the research work of the faculty
"""

import json
import requests
from bs4 import BeautifulSoup

data = json.loads(open("faculty-info.json").read())
baseurl = "https://jaipur.manipal.edu"
for x in data:

    for y in range(len(data[x])):
        try:
            url = baseurl + data[x][y]["url"]
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            div = soup.find("div", {"id": "research"})
            div = div.find("div")
            data[x][y]["research"] = eval(div["data-attr-research-json"])
        except:
            print("Error in ", x, y)
            continue

file = open("./json_data/research-faculty-info.json", "w")
file.write(json.dumps(data))

# open("test.txt", "w").write(soup.prettify())