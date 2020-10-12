#Write a Python program to find the three largest integers from a given list of numbers using Heap queue algorithm.
import heapq as hq
nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
print("Original list:")
print(nums_list)
# Find three largest values
largest_nums = hq.nlargest(3, nums_list)
print("\nThree largest numbers are:", largest_nums)

# Write a Python program to create an Enum object and display a member name and value.
from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('\nMember name: {}'.format(Country.Albania.name))
print('Member value: {}'.format(Country.Albania.value))
