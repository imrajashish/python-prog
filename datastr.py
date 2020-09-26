#Write a Python program to convert a float to ratio.
from fractions import Fraction
value = 4.2
print(Fraction(value).limit_denominator())

# Write a Python program to generate a series of unique random numbers.
import random
choices = list(range(100))
random.shuffle(choices)
print(choices.pop())
while choices:
    if input('Want another random number?(Y/N)' ).lower() == 'n':
        break
    print(choices.pop())
	