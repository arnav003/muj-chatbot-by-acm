import json
from bs4 import BeautifulSoup

data = json.loads(open("./json_data/research-faculty-info.json").read())
for x in data:
    for y in range(len(data[x])):
            try:
                url = "./pages/" + x + "/" + data[x][y]["url"].split("/")[-1]
                page = open(url, "r").read()
                soup = BeautifulSoup(page, 'html.parser')
                div = soup.find("div", {"id": "academic"})
                div = list(div.find_all("ul"))[1]
                data[x][y]["designation"] = [data[x][y]["designation"]] + [("".join(aa for aa in x.text if aa.isprintable()).strip()) for x in div.find_all("li")]
            except:
                data[x][y]["designation"] = [data[x][y]["designation"]]

file = open("./json_data/designation-research-data.json", "w")
file.write(json.dumps(data))
file.close()