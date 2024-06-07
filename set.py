var = {"Geeks", "for", "Geeks"}
print(var)

#Type Casting with Python Set method

myset=set(['a','n','c'])
print(myset)

myset.add('r')
print(myset)

# myset1={'a','r','n','o','b'}
# myset1[1]='r'
# print(myset1)

#frozen set
normalset={'a','r','n','o','b'}
print(normalset)
frozen=frozenset([1,2,3])
print(frozen)

#set add
people={"Jay","Idrish","Archil"}
print("People:",people)
people.add("Daxit")
print("After adding:",people)

#set union
people={"Jay","Idrish","Archil"}
vampires={"Karan","Arjun"}
population=people.union(vampires)
print("Union:",population)

#set intersection
people={"Jay","Idrish","Archil","Arnob"}
vampires={"Arnob","Karan","Arjun"}
population=people.intersection(vampires)
print("Intersection:",population)

#remove/disacard
population=people.remove("Arnob")
print("After removing:",people)

#pop
vampires={"Karan","Arjun"}
v=vampires.pop()
print("Vampire:",v)