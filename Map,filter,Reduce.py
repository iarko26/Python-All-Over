# map

def cube(x):return x*x*x

l=[1,2,3,4,5]
print(list(map(cube,l)))

# filter
def checkvowel(x):
    vowels=['a','e','i','o','u']
    return any([char in vowels for char in x.lower()])
   
    
checkname=["arnob","shakil","shahed","shahin","shahinur","hhhh"]
print(list(filter(checkvowel,checkname)))

#reduce
from functools import reduce
def add(a,b):
    return a+b  
l=[1,2,3,4,5]
print(reduce(add,l))