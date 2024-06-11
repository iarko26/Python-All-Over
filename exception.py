code='''
if(amount > 2999)
    print("You are eligible for a free gift")

'''

try:
    exec(code)
except SyntaxError:
    print("Syntax Error")


x=5
y="arnob"
try:
    z=x+y
except TypeError:
    print("Type Error")


#catching a specific exception

def add(n):
    if n>5:
        a=n/(n-5)
    print(a)

try:
    add(3)
    add(5)
except ZeroDivisionError:
    print("Zero Division Error")
except NameError:
    print("Name Error")

#try with else block
def myfunc(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("Zero Division Error")
    else:
        print(c)

myfunc(5,2)


    