#Write a Python program to convert JSON data to Python object.
import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"]) 

#Write a Python program to convert Python object to JSON data.
import json
# a Python object (dict):
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}
print(type(python_obj))
# convert into JSON:
j_data = json.dumps(python_obj)