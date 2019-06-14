import json
from pprint import pprint

with open("microsoft.json") as json_file:
    data = json.load(json_file)
#pprint(data)

#print(data["Time Series (Daily)"]['2019-06-07'])

for key, value in data["Time Series (Daily)"].items():
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            if sub_key=="2. high":
                print(key,sub_key,sub_value,sep=" | ")