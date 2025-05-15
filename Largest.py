#2.	Largest among the three using the binary minus operator
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if (a-b)>0 and (a-c)>0 :
    print(a,"is the largest number")
elif (b-a)>0 and (b-c)>0:
    print(b,"is largest number")
elif (c-a)>0 and (c-b)>0:
    print(c,"is largest number")
else:
    print("All numbers are equal")