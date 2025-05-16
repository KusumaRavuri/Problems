#7.	Roots of a quadratic equation
import cmath
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=(b*b)-4*a*c
sol1=(-b)+cmath.sqrt(d)/(2*a)
sol2=(-b)-cmath.sqrt(d)/(2*a)
print("The roots are:",sol1,sol2)