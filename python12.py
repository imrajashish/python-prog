#Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array?s contents and also find the size of the memory buffer in bytes.
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))

#Write a Python program to get the number of occurrences of a specified element in an array.
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(array_num))
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))
