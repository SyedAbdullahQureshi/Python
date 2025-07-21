a=5
print(a,type(a))
a=5.5
print(a,type(a))
a=2+5j
print(a,type(a))


s="Hello@123"
print(s,type(s))

s='''
Hello 
welcome to Cui 
'''
print(s)
#integer
s=10
print(s,type(s))
#string
s='10'
print(s,type(s))


##List

l=[10,'ws,5.5']
print(l,type(l))

#muteable
l=[10,'ws',5.5]
l[2]=10
print(l,type(l))


####All Data Types in Python

# Numeric Types
int_var = 42              # int
float_var = 3.14          # float
complex_var = 2 + 3j      # complex

# Text Type
str_var = "Hello, Python" # str

# Sequence Types
list_var = [1, 2, 3]           # list
tuple_var = (1, 2, 3)          # tuple
range_var = range(5)          # range

# Mapping Type
dict_var = {"name": "Alice", "age": 30}  # dict

# Set Types
set_var = {1, 2, 3}           # set
frozenset_var = frozenset([1, 2, 3])  # frozenset

# Boolean Type
bool_var = True              # bool

# Binary Types
bytes_var = b"hello"         # bytes
bytearray_var = bytearray(5) # bytearray
memoryview_var = memoryview(bytes_var) # memoryview

# None Type
none_var = None              # NoneType

# Print all types
print(type(int_var))
print(type(float_var))
print(type(complex_var))
print(type(str_var))
print(type(list_var))
print(type(tuple_var))
print(type(range_var))
print(type(dict_var))
print(type(set_var))
print(type(frozenset_var))
print(type(bool_var))
print(type(bytes_var))
print(type(bytearray_var))
print(type(memoryview_var))
print(type(none_var))
