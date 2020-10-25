#Write a Python program to remove all the elements of a given deque object. 
import collections
odd_nums = (1,3,5,7,9)
odd_deque  = collections.deque(odd_nums)
print("Original Deque object with odd numbers:")
print(odd_deque)
print("Deque length: %d"%(len(odd_deque)))
odd_deque.clear()
print("Deque object after removing all numbers-")
print(odd_deque)
print("Deque length:%d"%(len(odd_deque)))

#Write a Python program to count the number of times a specific element presents in a deque object.
import collections
nums = (2,9,0,8,2,4,0,9,2,4,8,2,0,4,2,3,4,0)
nums_dq = collections.deque(nums)
print("Number of 2 in the sequence")
print(nums_dq.count(2))
print("Number of 4 in the sequence")
print(nums_dq.count(4))

#Write a Python program to rotate a Deque Object specified number (positive) of times. 
import collections
# declare an empty deque object
dq_object = collections.deque()
# Add elements to the deque - left to right
dq_object.append(2)
dq_object.append(4)
dq_object.append(6)
dq_object.append(8)
dq_object.append(10)
print("Deque before rotation:")
print(dq_object)
# Rotate once in positive direction
dq_object.rotate()
print("\nDeque after 1 positive rotation:")
print(dq_object)
# Rotate twice in positive direction
dq_object.rotate(2)
print("\nDeque after 2 positive rotations:")
print(dq_object)

#. Write a Python program to rotate a Deque Object specified number (negative) of times. 
import collections
# declare an empty deque object
dq_object = collections.deque()
# Add elements to the deque - left to right
dq_object.append(2)
dq_object.append(4)
dq_object.append(6)
dq_object.append(8)
dq_object.append(10)
print("Deque before rotation:")
print(dq_object)
# Rotate once in negative direction
dq_object.rotate(-1)
print("\nDeque after 1 negative rotation:")
print(dq_object)
# Rotate twice in negative direction
dq_object.rotate(-2)
print("\nDeque after 2 negative rotations:")
print(dq_object)

