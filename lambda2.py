#Write a Python program to sort a list of dictionaries using Lambda.
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("\n originals dict in model:")
print(models)
sorted_models = sorted(models,key = lambda x:x['color'])
print(sorted_models)

#Write a Python program to filter a list of integers using Lambda.
nums = [1,23,24,65,97,87,98,89]
print("\n Original nums")
print(nums)
even_nums=list(filter(lambda x: x%2 ==0,nums))
print(even_nums)
odd_nums=list(filter(lambda x: x%2 !=0,nums))
print(odd_nums)

#Write a Python program to square and cube every number in a given list of integers using Lambda.
nums = [12,23,34,56,78,87]
print(nums)
square_nums = list(map(lambda x: x ** 2, nums))
print("\n square of nums:")
print(square_nums)
cube_nums = list(map(lambda x: x ** 3, nums))
print("\n cube of nums:")
print(cube_nums)

#Write a Python program to find if a given string starts with a given character using Lambda.
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Java'))

#Write a Python program to extract year, month, date and time using Lambda.
import datetime
now = datetime.datetime.now()
print(now)
year = lambda x : x.year
month = lambda x : x.month
date = lambda x : x.date
t = lambda x : x.time()
print(year(now))
print(month(now))
print(date(now))
print(t(now))

#Write a Python program to check whether a given string is number or not using Lambda.
is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))

#Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))
