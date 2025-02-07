try:
    number = 5
    print(number)
except:
    print("An error has occurred")
finally:
    print("Bye")

try:
    x = 67
    y = 0
    print(x/y)

except:
   print("ZeroDivisionError occurred")
