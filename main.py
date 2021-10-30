import json
with open("data.json") as file:
    data = json.load(file)

for i in data():
    print(i)
