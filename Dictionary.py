d={
    'course_name':'Python',
    'course_duration':'2 Month'

}
print(d['course_name'])
print(d,type(d))



# Dictionary


dev = {"name": "Ali Raza", "age": 28, "skill": "Python"}  # create

# Access
print(dev["name"])              # name
print(dev.get("skill"))         # skill

# Add
dev["city"] = "Lahore"          # add

# Update
dev["age"] = 29                 # update

# Delete
del dev["skill"]                # delete

# Loop
for key in dev:                 # loop
    print(key, ":", dev[key])   # print

# Methods
print(dev.keys())               # keys
print(dev.values())             # values
print(dev.items())              # items

# Check
print("city" in dev)            # check
