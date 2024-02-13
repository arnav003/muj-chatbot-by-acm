import json
from bs4 import BeautifulSoup

data = json.loads(open("./json_data/publications-designation-research-data.json").read())

def sanatize(element):
    return "".join(x for x in element if x.isprintable()).strip()

for x in data:
    for y in range(len(data[x])):
            count = 1
            try:
                url = "./pages/" + x + "/" + data[x][y]["url"].split("/")[-1]
                page = open(url, "r", encoding="utf-8", errors="replace").read()
                soup = BeautifulSoup(page, 'html.parser')
                div = soup.find("div", {"id": "expertise"})
                div = div.find("div", {"class": "row"})
                if div == None:
                    data[x][y]["expertise"] = []
                    continue

                data[x][y]["expertise"] = {}
                for a in div.find_all("p", {"class": "mb-3"}):
                    if count % 2 == 0:
                        data[x][y]["expertise"][prev] = sanatize(a.text)
                    else:
                        data[x][y]["expertise"][sanatize(a.text)] = ""
                        prev = sanatize(a.text)
                    count += 1

            except Exception as e:
                # data[x][y]["designation"] = []
                print(e, url)

file = open("./json_data/expertise-publications-designation-research-data.json", "w")
file.write(json.dumps(data))
file.close()

file = open("./json_data/final/data.json", "w")
file.write(json.dumps(data))
file.close()