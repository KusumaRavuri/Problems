#3.	Sum of two numbers without the + operator
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
while b != 0:
    carry = a & b
    a = a ^ b
    b = carry << 1
print(a)