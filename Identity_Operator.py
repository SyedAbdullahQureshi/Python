x=10
y=10
print(x is y,x==y)
print(x is not y)
print(x!=y)


x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True   (same)
print(x is z)      # False  (different)
print(x == z)      # True   (equal)

print(x is not z)  # True   (different)
