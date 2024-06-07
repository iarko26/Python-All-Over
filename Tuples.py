tup=(('dsa','dev','machine learning'))
print(tup)
# mytuple=(1,2,3,4,5)
# mytuple[2]=9
# print(mytuple)

#concat
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple3=tuple1+tuple2
print(tuple3)

#nesting
tuple4=(tuple1,tuple2)

#repeating
tuple5=('python',)*2
print(tuple5)
#slice
print(tuple1[1:])
print(tuple1[1:2])
print(tuple2[::-1])

#delete
del tuple4

#tuples in a loop
tupl=("java",)
n=3
for i in range(int(n)):
    tupl=(tupl,)
    print(tupl)
