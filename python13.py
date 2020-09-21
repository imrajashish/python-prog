#Write a Python program to insert a new item before the second element in an existing array
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Insert new value 4 before 3:")
array_num.insert(1, 4)
print("New array: "+str(array_num))

#Write a Python program to remove a specified item using the index from an array.
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Remove the third item form the array:")
array_num.pop(2)
print("New array: "+str(array_num))

#Write a Python program to remove the first occurrence of a specified element from an array.
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
print("Remove the first occurrence of 3 from the said array:")
array_num.remove(3)
print("New array: "+str(array_num))
