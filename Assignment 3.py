# Task 1
n=int(input("Enter The Number:"))
def factorial(n):
    if n < 1:
        return 1
    else:
        return n*factorial(n-1)
fact = factorial(n)
print("Factorial of",n,"is :",fact)
# Task 2
n=int(input("Enter a number:"))
from math import *
A=(sqrt(n))
B=(log(n))
C=(sin(n))
print("square root :",A)
print("logarithm :",B)
print("Sine :",C)
print("Thank you")
