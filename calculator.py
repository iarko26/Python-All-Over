number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
def add(number1,number2):
    return number1+number2
def subtract(number1,number2):
    return number1-number2
def multiply(number1,number2):
    return number1*number2
def divide(number1,number2):
    return number1/number2
def exp(number1,number2):
    return number1**number2
def flr(number1,number2):
    return number1//number2
def mod(number1,number2):
    return number1%number2
print("select operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Floor Division")
print("7. Modulus")

Operation=input("Enter operation number: ")
if Operation=="1":
    print("The Sum is:",add(number1,number2))
elif Operation=="2":
    print("The Difference is:",subtract(number1,number2))
elif Operation=="3":
    print("The Product is:",multiply(number1,number2))
elif Operation=="4":
    print("The Quotient is:",divide(number1,number2))
elif Operation=="5":
    print("The Exponent is:",exp(number1,number2))
elif Operation=="6":
    print("The Floor Division is:",flr(number1,number2))
elif Operation=="7":
    print("The Modulus is:",mod(number1,number2))

continue_=input("Do you want to continue? (yes/no): ")
if continue_=="yes":
    Operation=input("Enter operation number: ")
    if Operation=="1":
        print("The Sum is:",add(number1,number2))
    elif Operation=="2":
        print("The Difference is:",subtract(number1,number2))
    elif Operation=="3":
        print("The Product is:",multiply(number1,number2))
    elif Operation=="4":
        print("The Quotient is:",divide(number1,number2))
    elif Operation=="5":
        print("The Exponent is:",exp(number1,number2))
    elif Operation=="6":
        print("The Floor Division is:",flr(number1,number2))
    elif Operation=="7":
        print("The Modulus is:",mod(number1,number2))
else:
    print("Thank You!")







