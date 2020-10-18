#Write a Python program to create a heapsort, pushing all values onto a heap and then popping off the smallest values one at a time.
import heapq
def heapsort(h):
    heap = []
    for value in h:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for i in range(len(heap))]

print(heapsort([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))


#Write a Python program to get the two largest and three smallest items from a dataset.
import heapq
h = [10,20,06,30,405,06,70,80]
print(heapq.nsmallest(2,h))
print(heapq.nlargest(3,h))

#Write a Python program to locate the left insertion point for a specified value in sorted order.
import bisect
def index(a,x):
    i = bisect.bisect_left(a,x)
    return i
a = [1,2,3,4,5]
print(index(a,6))
print(index(a,3))

# Write a Python program to locate the right insertion point for a specified value in sorted orde
import bisect
def index(a, x):
    i = bisect.bisect_right(a, x)
    return i
    
a = [1,2,4,7]
print(index(a, 6))
print(index(a, 3))

#Write a Python program to insert items into a list in sorted order.
import bisect
my_list = [12,43,65,34,54,45,65,2,35,5,4]
print("Original list: ")
print(my_list)
sorted_list = []
for i in my_list:
    position = bisect.bisect(sorted_list,1)
    bisect.insort(sorted_list,i)
print("sorted list:")
print(sorted_list)

#a Python program to create a queue and display all the members and size of the queue.
import queue
q = queue.Queue()
for x in range(4):
    q.put(x)
print("Members of the queue:")
y=z=q.qsize()
for n in list(q.queue):
    print(n, end=" ")
print("\nSize of the queue:")
print(q.qsize())