import json
"""
# Python dict → JSON string
json_string = json.dumps(data, indent=2)
print(json_string)

# JSON string → Python dict
python_obj = json.loads(json_string)
print(python_obj["name"])

"""

user = {
    "name" : "ayush",
    "skills" : ["Python","Ai"]
}

test = json.dumps(user) 
print("User : ",test)
print("User JOSN : ",test)
back = json.loads(test)

