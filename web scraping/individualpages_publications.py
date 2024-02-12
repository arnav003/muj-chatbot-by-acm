import json
from bs4 import BeautifulSoup

data = json.loads(open("./json_data/designation-research-data.json").read())
for x in data:
    for y in range(len(data[x])):
            try:
                url = "./pages/" + x + "/" + data[x][y]["url"].split("/")[-1]
                page = open(url, "r", encoding="utf-8", errors="replace").read()
                soup = BeautifulSoup(page, 'html.parser')
                div = soup.find("div", {"id": "publications"})
                div = div.find("div")
                data[x][y]["publications"] = eval(div["data-attr-publication-json"])
            except Exception as e:
                # data[x][y]["designation"] = []
                print(e, url)

file = open("./json_data/publications-designation-research-data.json", "w")
file.write(json.dumps(data))
file.close()