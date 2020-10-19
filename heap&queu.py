#Write a Python program to find the three largest integers from a given list of numbers using Heap queue algorithm
import heapq
h = [12,34,56,786,56,45,3,453]
print("Three largest number in list: ")
print(heapq.nlargest(3,h))

#Write a Python program to find the three smallest integers from a given list of numbers using Heap queue algorithm.
import heap
h = [12,34,56,786,56,45,3,453]
print("original list",h)
print(heapq.nsmallest(3,h))

#Write a Python program to implement a heapsort by pushing all values onto a heap and then popping off the smallest values one at a time.
import heapq as hq
def heapsort(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for i in range(len(h))]
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

