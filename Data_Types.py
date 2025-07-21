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
ahmed = 42                     # int
bilal = 3.14                   # float
kashif = 2 + 3j                # complex

# Text Type
faizan = "Hello, Python"       # str

# Sequence Types
zahid_list = [1, 2, 3]              # list
yasir_tuple = (1, 2, 3)             # tuple
hamza_range = range(5)             # range

# Mapping Type
usman_dict = {"name": "Usman", "age": 30}  # dict

# Set Types
imran_set = {1, 2, 3}                  # set
noman_frozenset = frozenset([1, 2, 3])  # frozenset

# Boolean Type
saad = True                           # bool

# Binary Types
tariq_bytes = b"hello"                # bytes
adil_bytearray = bytearray(5)         # bytearray
nabeel_memoryview = memoryview(tariq_bytes)  # memoryview

# None Type
junaid = None                         # NoneType

# Print all types
print(type(ahmed))
print(type(bilal))
print(type(kashif))
print(type(faizan))
print(type(zahid_list))
print(type(yasir_tuple))
print(type(hamza_range))
print(type(usman_dict))
print(type(imran_set))
print(type(noman_frozenset))
print(type(saad))
print(type(tariq_bytes))
print(type(adil_bytearray))
print(type(nabeel_memoryview))
print(type(junaid))
