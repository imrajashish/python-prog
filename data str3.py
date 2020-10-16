#Write a Python program to compare two unordered lists (not sets).
from collections import Counter
def compare_lists(x,y):
    return Counter(x) == Counter(y)
n1 = [12,30,40,50,60]
n2 = [92,938,847,50,60]
print(compare_lists(n1,n2))

#Write a Python program to create an array contains six integers. Also print all the members of the array.
from array import array
my_array = ('i',[20,30,40,50,60,70,80,90])
for i in my_array:
    print(i)

#Write a Python program to get the array size of types unsigned integer and float.
from array import array
a = array("I", (12,25))
print(a.itemsize)
a = array("f", (12.236,36.36))
print(a.itemsize)

#Write a Python program to get an array buffer information.
from array import array
a = array("I",(12,25))
print("Array buffer start address in memory and number of elements.")
print(a.buffer_info())

#Write a Python program to get the length of an array.
from array import array
a = array("I",[21,23,23])
print(len(a))

#Write a Python program to convert an array to an ordinary list with the same items.
from array import array
a = array("b",[1,2,3,4,5])
print(a)
print("Array to list : ")
print(a.tolist())

#Write a Python program to push three items into the heap and print the items from the heap.
import heapq
heap = []
heapq.heappush(heap,('v',1))
heapq.heappush(heap,('v',2))
heapq.heappush(heap,('v',3))
for a in heap:
    print(a)

#Write a Python program to push three items into a heap and return the smallest item from the heap. Also Pop and return the smallest item from the heap.
import heapq
heap = []
heapq.heappush(heap, ('V', 3))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 1))
print("Items in the heap:")
for a in heap:
	print(a)
print("----------------------")
print("The smallest item in the heap:")
print(heap[0])
print("----------------------")
print("Pop the smallest item in the heap:")
heapq.heappop(heap)
for a in heap:
	print(a)