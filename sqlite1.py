#Write a Python program to triple all numbers of a given list of integers. Use Python map.
nums = (1, 2, 3, 4, 5, 6, 7) 
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))

#Write a Python program to add three given lists using Python map and lambda.
nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
nums3 = [7, 8, 9] 
print("Original list: ")
print(nums1)  
print(nums2)  
print(nums3)  
result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3) 
print("\nNew list after adding above three lists:")
print(list(result))
