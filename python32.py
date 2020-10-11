#Write a Python program to find the first duplicate element in a given array of integers. Return -1 If there are no such elements.
def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate

print(find_first_duplicate([1, 2, 3, 4, 4, 5]))
print(find_first_duplicate([1, 2, 3, 4]))
print(find_first_duplicate([1, 1, 2, 3, 3, 2, 2]))

#Write a Python program to find whether a given array of integers contains any duplicate element. Return true if any value appears at least twice in the said array and return false if every element is distinct.
def test_duplicate(array_nums):
    nums_set = set(array_nums)    
    return len(array_nums) != len(nums_set)     
print(test_duplicate([1,2,3,4,5]))
print(test_duplicate([1,2,3,4, 4]))
print(test_duplicate([1,1,2,2,3,3,4,4,5]))
