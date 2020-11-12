#Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
class py_solution:
       def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i )
            lookup[num] = i
print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))
