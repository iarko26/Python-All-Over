try:
    num=int(input("Enter a number: "))
    if num<0:
        print("Negative number")
    else:
        print("Positive number")
except ValueError:
    print("Value Error")
finally:
    print("This is finally block")