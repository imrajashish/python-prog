#Write a Python program to create a deque and append few elements to the left and right, then remove some elements from the left, right sides and reverse the deque
import collections
# Create a deque
deque_colors = collections.deque(["Red","Green","White"])
print(deque_colors)
# Append to the left
print("\nAdding to the left: ")
deque_colors.appendleft("Pink")
print(deque_colors)
# Append to the right
print("\nAdding to the right: ")
deque_colors.append("Orange")
print(deque_colors)
# Remove from the right
print("\nRemoving from the right: ")
deque_colors.pop()
print(deque_colors)
# Remove from the left
print("\nRemoving from the left: ")
deque_colors.popleft()
print(deque_colors)
# Reverse the dequeue
print("\nReversing the deque: ")
deque_colors.reverse()
print(deque_colors)

#Write a Python program to create a deque from an existing iterable object. 
import collections
even_nums = (2, 4, 6)
print("Original tuple:")
print(even_nums)
print(type(even_nums))
even_nums_deque = collections.deque(even_nums)
print("\nOriginal deque:")
print(even_nums_deque)
even_nums_deque.append(8)
even_nums_deque.append(10)
even_nums_deque.append(12)
even_nums_deque.appendleft(2)
print("New deque from an existing iterable object:")
print(even_nums_deque)
print(type(even_nums_deque))


#Write a Python program to add more number of elements to a deque object from an iterable object.
import collections
even_nums = (2, 4, 6, 8, 10)
even_deque = collections.deque(even_nums)
print("Even numbers:")
print(even_deque)
more_even_nums = (12, 14, 16, 18, 20)
even_deque.extend(more_even_nums)
print("More even numbers:")
print(even_deque)