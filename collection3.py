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

#Write a Python program to find the most common element of a given list.
from collections import Counter
language = ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python','PHP', 'Python']
print("Original list:")
print(language)
cnt = Counter(language)
print("\nMost common element of the said list:")
print(cnt.most_common(1)[0][0])

#Write a Python program to perform Counter arithmetic and set operations for aggregating results.
import collections
c1 = collections.Counter([1, 2, 3, 4, 5])
c2 = collections.Counter([4, 5, 6, 7, 8])
print('C1:', c1)
print('C2:', c2)
print('\nCombined counts:')
print(c1 + c2)
print('\nSubtraction:')
print(c1 - c2)
print('\nIntersection (taking positive minimums):')
print(c1 & c2)
print('\nUnion (taking maximums):')
print(c1 | c2)

#