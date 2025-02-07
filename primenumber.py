# A programme to check whether a number is a prime number (user input)
number = int(input("Enter a number: "))
if number > 1 :
    for i in range(2,number):
        if number % i == 0:
            print("number is not prime")
            break
    else :
        print("number is prime")

else :
    print("number is not prime")