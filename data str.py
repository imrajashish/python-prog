#Write a Python program to create an Enum object and display a member name and value.
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

#Write a Python program to display all the member name of an enum class ordered by their values.
from enum import IntEnum
class Country(IntEnum):
    japan = 100
    india = 7733
    odisha = 273
    bihar = 84
country_code_list = list(map(int, Country))
print(country_code_list)
