import math
## Calculator App

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /, ^): ")
result = 0
if operation == "+":
    result = x + y

if operation == "-":
    result = x - y

if operation == "*":
    result = x * y

if operation == "/":
    result = x / y

if operation == "^":
    result =  pow(y, x) # Design feature

if operation == "sin":
    result = math.sin(x)


print(result)