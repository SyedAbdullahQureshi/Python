t=(5,'program',1+3j)
print(t,type(t))
t=(10,20,'Hello')
print(t,type(t))
t=10
print(t,type(t))


#tuples_in_python_demo.py


# Create
data = ("NxGen", 30, "Developer")  # tuple

# Access
print(data[0])                    # name
print(data[1])                    # age

# Length
print(len(data))                  # length

# Loop
for item in data:                 # loop
    print(item)                   # print

# Unpack
name, age, role = data            # unpack
print(name)                       # name
print(age)                        # age
print(role)                       # role

# Nest
info = (data, ("USA", "Pakistan"))      # nested
print(info[1][1])                 # city
