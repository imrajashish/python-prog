#Write a Python program to iterate over sets.
num_set =([12,32,44,56,78,9,0,76,78,55])
for n in num_set:
    print(n)

#Write a Python program to add member(s) in a set.
s = set([12,23,43,54,65,66])
s.add(60)
print(s)
s.update([343,87])
print(s)

#Write a Python program to remove item(s) from set
num_set = set([0, 1, 3, 4, 5])
num_set.pop()
print(num_set)
num_set.pop()
print(num_set)

#Write a Python program to create an intersection of sets


#Write a Python program to remove an item from a set if it is present in the set
num_set = set([12,32,43,45,665])
num_set.discard(45)
print(num_set)

#Write a Python program to create an intersection of sets
num1 = set(["red","green","blue"])
num2 = set(["orange","green","white"])
num3 = num1 & num2
num4 = num1 | num2
print(num4)
print(num3)

#Write a Python program to create a union of sets
num1 = set([12,263,4847,38374])
num2 = set([121,232,445,54543])
num3 = num1|num2
print(num3)

#Write a Python program to create set difference.
num1 = set([4132,1,2,3,4])
num2 = set([625,1,2,3,4])
num3 = num1-num2
print(num3)

#Write a Python program to create a symmetric difference.
num1 = set([4132,1,2,3,4])
num2 = set([625,1,2,3,4])
num3 = num1^num2
print(num3)

#Write a Python program to check if a set is a subset of another set
num1 = set([1,2,3,4])
num2 = set([1,2,3,4])
num3 = num1<=num2
print(num3)

# Write a Python program to create a shallow copy of sets.
num1 = set([1,2,3,4,366234])
num2 = set([1,2,3,4,736])
num3 = num1.copy()
print(num3)
