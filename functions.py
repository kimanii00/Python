# Built-in functions/Standard library functions
from Variable import firstname

y = max(67,43,89,90,23)
print("The maximum value is ",y)

x = min (15,3,20,78)
print("The minimum value is ",x)

# User-defined Functions
def name ():
    print("Samantha")

name() # Calling a function

def multiply():
    x = 10
    y = 2
    print(x * y)
multiply()

# Parameter/Variable and Argument/Value assigned to a parameter
def add (a,b) :
    print(a + b)

add(1,4)
add(6,7)

def employee(name,gender,position,salary,age):
    print(name,gender,position,salary,age)

employee("Samantha","Female","CEO",5600000,30)
employee("John","Male","Managing Director",4600000,25)
employee("Mary","Female","HR",3500000,35)

#A programme that displays details of 5 students
# Use a user-defined function with the help of parameters and arguments
# Fullname,age,course,gender

def student(fullname,age,course,gender):
    print(fullname,age,course,gender)

student("frank castle",20,"MIT","Male")
student("Stacy Nyambura",19,"MIT","female")
student("Kyle Kimani", 17,"Cybersecurity","Male")
student("Anna Nicole", 18,"Datascience","female")
student("Zeinab Mohammed", 21,"Cybersecurity","female")


