x=10
y=20
print(x==y)


print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)


#comparoson operator

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Equal
print("x == y:", x == y)

# NotEqual
print("x != y:", x != y)

# Greater
print("x > y:", x > y)

# Less
print("x < y:", x < y)

# GreaterEqual
print("x >= y:", x >= y)

# LessEqual
print("x <= y:", x <= y)


###Logical_Operator Starts:-



x=10
y=20

print(x==10 and x<y)
# not correct is ma dono traf logic lagia howa ha
# print(x==10 and x<y and x==y)

print(x!=10 or x<y and x==y)
print(x!=10)
print(not x!=10)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Condition1
cond1 = (a > 10)

# Condition2
cond2 = (b < 20)

# OR
print("OR:", cond1 or cond2)

# AND
print("AND:", cond1 and cond2)

# NOT
print("NOT cond1:", not cond1)
print("NOT cond2:", not cond2)
