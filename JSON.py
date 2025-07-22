#=> what is JSON?
{
  "name": "Ali",
  "age": 30,
  "is_student": false
}

#=> Create JSON File

import json
data = {
 "name":"Ali",
  "age":30,
  "is_student": False
}

# => Write JSON ti file
with open("data.jason","w") as json_file:
  jsonn.dump(data, json_file, indent=4)


# => Converting Json Data to Python Object
#during converstion of JSON string into a Python object, use json.loads().
import json
jason_data = '{"name": "Ali":"agr":30,"is_student": false}'
# => Convert JSON string to Python dict
python_obj = json.loads(json_data)

print(python_obj)
print(python_obj["name"])  # Output: Alice

# => Read JSON File
import json

# Read JSON from a file

with open("data.json", "r") as json_file:
    data = json.load(json_file)

print(data)

# => Write to JSON File

new_data = {
    "city": "New York",
    "temperature": 25
}

with open("weather.json", "w") as file:
    json.dump(new_data, file, indent=4)
