#Write a Python function which accepts an arbitrary list and converts it to a heap using Heap queue algorithm.
import heapq as hq
h = [12,23,34,34,54,45,76,87,98.9]
print("Raw Heap:",h)
hq.heapify(h)
print("\nHeap ify(heap):",h)

#Write a Python program to delete the smallest element from the given Heap and then inserts a new item
import heapq as hq

heap = [25, 44, 68, 21, 39, 23, 89]
hq.heapify(heap)
print("heap: ", heap)
hq.heapreplace(heap, 21)
print("heapreplace(heap, 21): ", heap)
hq.heapreplace(heap, 110)
print("heapreplace(heap, 110): ", heap)

#Write a Python program to sort a given list of elements in ascending order using Heap queue algorithm.
import heapq as hq
h = [1,43,23,54,56,87,54,334,564,23,45,66,4]
print("original list: ")
print(h)
hq.heapify(h)
s_result = [hq.heappop(h) for i in range(len(h))]
print("\n sorted list: ")
print(s_result)

#Write a Python program to find the kth (1 <= k <= array's length) largest element in an unsorted array using Heap queue algorithm.
import heapq

class Solution(object):
    def find_Kth_Largest(self, nums, k):
        """
        :type nums: List[int]
        :type of k: int
        :return value type: int
        """
        h = []
        for e in nums:
            heapq.heappush(h, (-e, e))
        for i in range(k):
            w, e = heapq.heappop(h)
            if i == k - 1:
                return e

arr_nums = [12, 14, 9, 50, 61, 41]
s = Solution()
result = s.find_Kth_Largest(arr_nums, 3)
print("Third largest element:",result)
result = s.find_Kth_Largest(arr_nums, 2)
print("\nSecond largest element:",result)
result = s.find_Kth_Largest(arr_nums, 5)
print("\nFifth largest element:",result)

#Write a Python program to compute maximum product of three numbers of a given array of integers using Heap queue algorithm.
def maximumproduct(nums):
    import heapq
    a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
    return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])
arr_nums = [64,84,3,43,2,34]
print("original array elements:")
print(arr_nums)
print("Maximum product of three numbers of the said array:")
print(maximumproduct(arr_nums))    

    