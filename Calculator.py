# A simple calculator programme
from random import choice


def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
print("Please select an operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter your choice(1/2/3/4): ")
if choice in ("1","2","3","4"):
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please try again.")

    if choice == "1":
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice == "2":
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice == "3":
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice == "4":
        print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid input")

