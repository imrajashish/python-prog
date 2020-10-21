#Write a Python program to find the top k integers that occur the most frequently from a given lists of sorted and distinct integers using Heap queue algorithm.
def func(nums, k):
    import collections
    d = collections.defaultdict(int)
    for row in nums:
        for i in row:
            d[i] += 1
    temp = []
    import heapq
    for key, v in d.items():
        if len(temp) < k:
            temp.append((v, key))
            if len(temp) == k:
                heapq.heapify(temp)
        else:
            if v > temp[0][0]:
                heapq.heappop(temp)
                heapq.heappush(temp, (v, key))
    result = []
    while temp:
        v, key = heapq.heappop(temp)
        result.append(key)
    return result
nums = [
      [1, 2, 6],
      [1, 3, 4, 5, 7, 8],
      [1, 3, 5, 6, 8, 9],
      [2, 5, 7, 11],
      [1, 4, 7, 8, 12]
    ]  
k = 3
print("Original lists:")
print(nums)
print("\nTop 3 integers that occur the most frequently in the said lists:")
print(func(nums, k))

#Write a Python program to get the n expensive and cheap price items from a given dataset using Heap queue algorithm.
import heapq
from pprint import pprint
items = [
    {'name': 'Item-1', 'price': 101.1},
    {'name': 'Item-2', 'price': 555.22},
    {'name': 'Item-3', 'price': 45.09},
    {'name': 'Item-4', 'price': 22.75},
    {'name': 'Item-5', 'price': 16.30},
    {'name': 'Item-6', 'price': 110.65}
]

cheap = heapq.nsmallest(3, items, key=lambda s: s['price'])
expensive = heapq.nlargest(3, items, key=lambda s: s['price'])
print("Original datasets:")
pprint(items)
print("\nFirst 3 expensive items:")
pprint(expensive)
print("\nFirst 3 cheap items:")
pprint(cheap)

#Write a Python program to merge multiple sorted inputs into a single sorted iterator (over the sorted values) using Heap queue algorithm
import heapq
num1 = [12,42,35,66,6,4,32,13,3434]
num2 = [32,454,565,3,23,312,04]
num3 = [212,454,3,443,3,122,3232]
num1 = sorted(num1)
num2 = sorted(num2)
num3 = sorted(num3)
result = heapq.merge(num1,num2,num3)
print(list(result))

#Given a n x n matrix where each of the rows and columns are sorted in ascending order, write a Python program to find the kth smallest element in the matrix.
import heapq
class Solution(object):
    def find_Kth_Smallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        m, n = len(matrix), len(matrix[0])
        temp = [[False] * n for _ in range(m)]
        q = [(matrix[0][0], 0, 0)]
        ans = None
        temp[0][0] = True
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if i + 1 < m and not temp[i + 1][j]:
                temp[i + 1][j] = True
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not temp[i][j + 1]:
                temp[i][j + 1] = True
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans

matrix = [
   [0, 5, 9],
   [11, 12, 13],
   [15, 17, 19]   
]
k = 1
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("First smallest element:",result)
k = 2
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("\nSecond smallest element:",result)
k = 3
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("\nThird smallest element:",result)

#Write a Python program to find the nth super ugly number from a given prime list of size k using Heap queue algorithm
import heapq
#Ref.: https://bit.ly/32c9P3A
def nth_Super_Ugly_Number(n, primes):
    uglies = [1]

    def gen(prime):
        for ugly in uglies:
            yield ugly * prime

    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]
n = 12
primes = [2,7,13,19]
print(nth_Super_Ugly_Number(n, primes))


#Write a Python program to get the k most frequent elements from a given non-empty list of words using Heap queue algorithm.
import heapq
from collections import Counter
class Solution:
    def top_K_Frequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :return type: List[str]
        """
        ctr = Counter(words)
        heap = [(-ctr[word], word) for word in ctr]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

if __name__ == '__main__':
    words = ["a", "abc", "abcdef", "a", "abcd", "abcd", "abc", "abcdefg"]
    k = 3
    s = Solution()
    print("3 most frequent elements:")
    print(s.top_K_Frequent(words, k))

#Write a Python program to check if the letters of a given string can be rearranged so that two characters that are adjacent to each other are different using Heap queue algorithm.
import heapq
from collections import Counter
def reorganizeString(S):
    ctr = Counter(S)
    heap = [(-value, key) for key, value in ctr.items()]
    heapq.heapify(heap)
    if (-heap[0][0]) * 2 > len(S) + 1: 
        return ""
    ans = []
    while len(heap) >= 2:
        nct1, char1 = heapq.heappop(heap)
        nct2, char2 = heapq.heappop(heap)
        ans.extend([char1, char2])
        if nct1 + 1: heapq.heappush(heap, (nct1 + 1, char1))
        if nct2 + 1: heapq.heappush(heap, (nct2 + 1, char2))
    return "".join(ans) + (heap[0][1] if heap else "")

print(reorganizeString("aab"))
print(reorganizeString("abc"))
print(reorganizeString("aabb"))
print(reorganizeString("abccdd"))
