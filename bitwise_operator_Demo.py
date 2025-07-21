x=10
y=8
print(bin(x))
print(bin(y))
print(bin(x&y),x&y)
print(bin(x|y),x|y)
print(bin(x^y),x^y)
#0b1010
#0b1000

#& 1000   8
#& 1010   10
#^ 0010   2


##bitwise_operator_Demo.py

a = 10         # number
b = 4          # number

print("a =", a, "=>", bin(a))       # binary
print("b =", b, "=>", bin(b))       # binary
print()

and_result = a & b                 # AND
print("1. AND:", bin(a), "&", bin(b), "=", bin(and_result), "=>", and_result)  # result
print()

or_result = a | b                  # OR
print("2. OR:", bin(a), "|", bin(b), "=", bin(or_result), "=>", or_result)     # result
print()

xor_result = a ^ b                 # XOR
print("3. XOR:", bin(a), "^", bin(b), "=", bin(xor_result), "=>", xor_result)  # result
print()

not_result = ~a                   # NOT
print("4. NOT:", "~", bin(a), "=", bin(not_result), "=>", not_result)         # result
print()

# Summary
print("Summary:")                 # summary
print("a =", a, "=>", bin(a))     # display
print("b =", b, "=>", bin(b))     # display
print("a & b =", and_result, "=>", bin(and_result))  # display
print("a | b =", or_result, "=>", bin(or_result))    # display
print("a ^ b =", xor_result, "=>", bin(xor_result))  # display
print("~a =", not_result, "=>", bin(not_result))     # display
