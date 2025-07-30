import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
# print(einstein_json)
# pprint(back_to_dict)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)  # Takes the csv file f and converts it to a dictionary of dictionaries? Not sure what this does
    laureates = list(reader)  # a list of dictionaries that were saved in variable 'reader' using the csv command on previousl lines

# print(type(laureates))
print(type(reader))

# 1. you can access parts of strings the same way you do lists
#      hey[2] == "y"
# 2. You can add to a list using
#      my_list.append("something")

laureates_beginning_with_a = []
# LinkedIn learner code here
for name_with_a in laureates:
    if name_with_a["name"][0] == "A":  #accesses the "name" field of dictionarie and check for the first letter [0] if it's equal to "A"
        laureates_beginning_with_a.append(name_with_a)


with open("laureates.json", "w") as f:
    json.dump(laureates_beginning_with_a, f, indent=2)


