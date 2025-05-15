#1.	ASCII value of a given digit
digit=input("Enter the number: ")
if digit.isdigit():
    ascii_value=ord(digit)
    print("The ASCII value of the given number is:",ascii_value)
else:
    print("Invalid")