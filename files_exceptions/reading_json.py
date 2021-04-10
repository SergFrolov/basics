# This python code will read the json file

import json

#here we use path directly in the "with open" statement
with open("/Users/Serja_boi/dev/basics/advanced1/person.json") as file:
    data = json.load(file)
    # json.load is a function to read json file

print(data)
