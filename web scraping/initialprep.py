"""
Creates the faculty-info.json file which contains the faculty
    information of all the schools except school of law
"""
link = [
    ["foe", "https://jaipur.manipal.edu/foe/schools-faculty/faculty-list.html"],
    ["fos", "https://jaipur.manipal.edu/fos/schools-faculty/faculty-list.html"],
    ["fod", "https://jaipur.manipal.edu/fod/schools-faculty/faculty-list.html"],
    ["foa", "https://jaipur.manipal.edu/foa/schools-faculty/faculty-list.html"],
    ["fom", "https://jaipur.manipal.edu/fom/schools-faculty/faculty-list.html"],
]

import json
import requests
from bs4 import BeautifulSoup
data = {}


for x in link:
    page = requests.get(x[1])
    soup = BeautifulSoup(page.content, 'html.parser')

    # html div with id as container
    container = soup.find("section", class_="faculty-listing")
    div = container.find("div", class_="container")
    ul = div.find("ul")
    
    data[x[0]] = eval(ul["data-faculty-object"])
    
file = open("./json_data/faculty-info.json", "w")
file.write(json.dumps(data))