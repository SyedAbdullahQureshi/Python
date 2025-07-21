string="Hello"
print('H'in string)

l=[10,20,30,40]

print(50 in l)
print(50 not in l)
print(40 not in l)
print(40 in l)

#Example

# List
names = ["Ali", "Sara", "Usman"]     # list
print("Ali" in names)                # True
print("Ayesha" in names)             # False

# String
text = "Pakistan Zindabad"          # string
print("Zindabad" in text)           # True
print("India" not in text)          # True

# Set
skills = {"Python", "Java"}         # set
print("Python" in skills)           # True
print("C++" not in skills)          # True

# Tuple
marks = (85, 90, 95)                # tuple
print(90 in marks)                  # True
print(100 not in marks)             # True

# Dictionary (checks keys only)
student = {"name": "Adeel", "age": 22}  # dict
print("name" in student)           # True
print("Adeel" in student)          # False (value, not key)
