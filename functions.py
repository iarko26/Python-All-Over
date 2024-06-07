# #create a functions
# def my_func():
#     print('Hello World')
# my_func()
# # functions with arguments

# def my_func(num1:int,num2:int)->int:
#     num3=num1+num2
#     return num3
# print(my_func(2,3))

# def isPrime(n):
#     for i in range(2,n):
#         if n%i==0 and n!=1:
#             return False
#         return True
# print(isPrime(78))
# print(isPrime(79))

# #default arguments
# def de_func(x,y=10):
#     print(x)
#     print(y)
# de_func(50)

# #positional arguments
# def nameAge(name,Age):
#    print(name) 
#    print(Age)

# print("case-1")
# nameAge("Arnob",22)
# print("case-2")
# nameAge(22,"Arnob")
# #docstring
# def evenodd(x):
#     '''Function to check if the number is even or odd'''
#     if(x%2==0):
#         print("even")
#     else:
#         print("odd")

# print(evenodd.__doc__);

#functions within function
def func1():
    print("this is python")
    def func2():
        print("this is java")
    func2()
func1()
