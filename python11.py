#Write a Python program to append items from a specified list.
from array import *
num_list = [1, 2, 6, -8]
array_num = array('i', [])
print("Items in the list: " + str(num_list))
print("Append items from the list: ")
array_num.fromlist(num_list)
print("Items in the array: "+str(array_num))

#Write a Python program to insert a new item before the second element in an existing array.
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Insert new value 4 before 3:")
array_num.insert(1, 4)
print("New array: "+str(array_num))
