#Write a Python program to iterate over an enum class and display individual member and their value.
from enum import Enum
class country(Enum):
    Afganistan = 10
    japan = 12
    india = 232
    odisha = 21
    Bihar = 121
for data in country:
    print('{:15} = {}'.format(data.name, data.value))
#Write a Python program to get all values from an enum class.
from enum import IntEnum
class country(IntEnum):
    India = 90
    japan = 20
    pakistan = 0
    morishash = 21
    patna = 23
country_code_list = list(map(int,country))
print(country_code_list)

#Write a Python program to count the most common words in a dictionary.
words = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]
from collections import Counter
word_counts = Counter(words)
top_four = word_counts.most_common(4)
print(top_four)