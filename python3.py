#Write a Python program to get the number of occurrences of a specified element in an array.
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(array_num))
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))

#Write a Python program to append items from inerrable to the end of the array. 
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
array_num.extend(array_num)
print("Extended array: "+str(array_num))
