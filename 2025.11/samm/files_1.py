import pickle
import string
import os

numbers = [1,2,3,4,5]

serialized_data = pickle.dumps(numbers)
print(f"serialized_data:\n {serialized_data}")

deserialized_data = pickle.loads(serialized_data)
print(f"deserialized_data: {deserialized_data}")

def creete_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    print(script_dir)
    return os.path.join(script_dir, file_name)

print(creete_path("contacts.txt"))

def deserialize(file_name):
    with open(creete_path(file_name),'rb') as file:
        data = pickle.load(file)
    return data

try:
    letters = [symbol for symbol in string.ascii_letters]
    file_name = "letters.data"

    print(f"Original data:\n {letters}")
    #serialize(file_name,letters)
    letters_restored = deserialize(file_name)
    print(f"deserialized_data:\n {letters_restored}")

except Exception as ex:
    print(ex)


import  json

caapitals = {
    "Italy": "Roma",
    "Spain": "Madrid",
    "Germabi": "Berlin"
}

s_capitals = json.dumps((caapitals))
print(f" old capitals: {caapitals}")
print(f"serial capitals: {s_capitals}")

print(json.loads(s_capitals))

def json_serialize(file_name,data):
    with open(creete_path(file_name),'w') as fle:
        json.dump(data,fle,indent=4)

print(creete_path("contacts.txt"))

def json_deserialize(file_name):
    with open(creete_path(file_name),'r') as file:
        data = json.load(file)
    return data

try:
    file_name = "employee.data"

    employees_dict = {
        "company": "Apple",
        "employees":[
            {
                "name":"Tim Cook",
                "age": 55,
                "skills": ["programing","comunicacion","crm"]
            }
        ]
    }
    json_serialize(file_name,employees_dict)
    des_dict = json_deserialize(file_name)
    print(f"before saving: {employees_dict}")
    print(f"After saving: {des_dict}")
except Exception as ex:
    print(ex)




