#Write a Python program to clear a set
num_set = set([12,23,23,243,221221,22,3,3])
print("Num_set",num_set)
num_set.clear()
print(num_set)

#Write a Python program to use of frozensets.
x = frozenset([1,2,3,4,5])
y = frozenset([3,4,5,6,7])
print(x.isdisjoint(y))
print(x.difference(y))
print(x|y)

#Write a Python program to find maximum and the minimum value in a set.
s = set([1223,2212,33455,33235,332434])
print(min(s))
print(max(s))

#Write a Python program to find the length of a set.
s = set(["rahul","suman","ravi"])
print(len(s))

#Write a Python program to check if a given value is present in a set or not.
nums = {3,4,5,6,7,8,8}
print(6 in nums)

#Write a Python program to check if two given sets have no elements in common.
x = {1,2,3,4}
y = {4,5,6,7,8}
z = {8}
print("compair x and y: ")
print(x.isdisjoint(y))
print("compair z and z: ")
print(z.isdisjoint(x))
print("Compair y and z: ")
print(y.isdisjoint(z))

#Write a Python program to check if a given set is superset of itself and superset of another given set.
nums = {10,20,30,40,50}
print("Original set: ",nums)
print("If nums is superset of itself?")
print(nums.issuperset(nums))
num1 = {1, 2, 3, 4, 5, 7}
num2 = {2, 4}
num3 = {2, 4}
print("\nnum1 = ", num1)
print("num2 = ", num2)
print("num3 = ", num3)
print("If mum1 is superset of num2:")
print(num1>num2)
print("Compare mum2 and num3:")
print("If mum2 is superset of num3:")
print(num2>num3)
print("If mum3 is superset of num2:")
print(num3>num2)

#Write a Python program to find the elements in a given set that are not in another set. 
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("difference of sn1 and sn2 using difference:")
print(sn1.difference(sn2))
print("difference of sn2 and sn1 using difference:")
print(sn2.difference(sn1))
print(sn1-sn2)
print(sn2-sn1)

#Write a Python program to remove the intersection of a 2nd set from the 1st set.
num1 = set([1,2,3,4,5,6])
num2 = set([4,5,6,7,8,9])
num3 = num2 - num1
print(num3)

#Write a Python program to check a given set has no elements in common with other given set.
sn1 = {1,2,3}
sn2 = {4,5,6}
sn3 = {3}
print("Original sets:")
print(sn1)
print(sn2)
print(sn3)
print("Check sn1 set has no elements in common with sn2 set:")
print(sn1.isdisjoint(sn2))
print("Check sn1 set has no elements in common with sn3 set:")
print(sn1.isdisjoint(sn3))
