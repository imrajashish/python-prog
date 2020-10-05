#Write a Python program to convert Python objects into JSON strings. Print all the values.
import json
python_dict =  {"name": "David", "age": 6, "class":"I"}
python_list =  ["Red", "Green", "Black"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
python_N =  (None)

json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_str = json.dumps(python_str)
json_num1 = json.dumps(python_int)
json_num2 = json.dumps(python_float)
json_t = json.dumps(python_T)
json_f = json.dumps(python_F)
json_n = json.dumps(python_N)

print("json dict : ", json_dict)
print("jason list : ", json_list)
print("json string : ", json_str)
print("json number1 : ", json_num1)
print("json number2 : ", json_num2)
print("json true : ", json_t)
print("json false : ", json_f)
print("json null ; ", json_n)

#Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4. 
import json
j_str = {'4' : 5,'6' : 7,'2' : 3,'8' : 32}
print("original string: ")
print(j_str)
print("\n JSON data: ")
print(json.dumps(j_str, sort_keys= True,indent= 4))

#Write a Python program to convert JSON encoded data into Python objects.
import json

jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
jobj_list =   '["Red", "Green", "Black"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float =  '21.34'
python_dict =  json.loads(jobj_dict)
python_list = json.loads(jobj_list)
python_str =  json.loads(jobj_string)
python_int =   json.loads(jobj_int)
python_float = json.loads(jobj_float)

print("Python dictionary: ", python_dict)
print("Python list: ", python_list)
print("Python string: ", python_str)
print("Python integer: ", python_int)
print("Python float: ", python_float)

#Write a Python program to check whether an instance is complex or not.
import json

def encode_complex(object):
    # check using isinstance method
    if isinstance(object, complex):
        return [object.real, object.imag]
    # raised error if object is not complex
    raise TypeError(repr(object) + " is not JSON serialized")

complex_obj = json.dumps(2 + 3j, default=encode_complex)
print(complex_obj) 

#Write a Python program to check whether a JSON string contains complex object or not.
import json
def is_complex_num(objct):
    if '__complex__' in objct:
        return complex(objct['real'], objct['img'])
    return objct

complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = is_complex_num)
simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
print("Complex_object: ",complex_object)
print("Without complex object: ",simple_object)

#Write a Python program to access only unique key value of a Python object
import json
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:")
print(python_obj)
json_obj = json.loads(python_obj)
print("\nUnique Key in a JSON object:")
print(json_obj) 
