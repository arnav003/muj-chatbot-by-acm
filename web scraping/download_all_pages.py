"""
This file downloads all the individual faculty pages listed on the faculty-info.json file
examples: https://jaipur.manipal.edu/content/muj/academics/institution-list/foe/schools-faculty/faculty-list/Ashish-Kumar.html

Scrape the downloaded pages for the speed and efficiency of the code.
"""

import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path

data = json.loads(open("faculty-info.json").read())
baseurl = "https://jaipur.manipal.edu"

for x in data:
    print(x, len(data[x]))
    for y in range(len(data[x])):
        try:
            url = baseurl + data[x][y]["url"]
            if Path(f"./pages/{x}/{url.split('/')[-1]}").exists():
                continue
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            open(f"./pages/{x}/{url.split('/')[-1]}", "w", encoding="utf-8").write(soup.prettify())
        except Exception as e:
            print("Error in ", e, url)
            continue