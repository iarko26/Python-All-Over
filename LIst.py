#create a List

list1=[1,2,3,3,4,"Arnob",True,1.2]
print(list1)

#access
print(list1[0])
print(list1[5])

#multidimensional list
list2=[["arnob",1,2],["ariyan",3,4],1,2]
print(list2[1][0])
print(list2[0][0])

#negative indexing
print(list1[-1])



#append
list1.append("Python")
print(list1)

list1.insert(2,"java")
print(list1)

#reverse
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)

list4=[1,2,3,4,5]
mylist=list(reversed(list4))
print(mylist)

list4.remove(3)
print(list4)

list4.pop(2)
print(list4)

list5=["arnob","ariyan","python","java"]
test=list(map(list,list5))
print(test)

#slicing
print(list5[1:3])
print(list5[1:])
print(list5[:3])
print(list5[0:3:2])

#list comprehension
l=[i*i for i in range(10) if i%2==0]
print(l)