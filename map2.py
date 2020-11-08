#Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
base_num = [10,20,30,40,50]
index = [1,2,3,4,5]
print("original list:")
print(base_num)
print(index)
result = list(map(pow, base_num ,index))
print("\nPower of said number in bases raised to the corresponding number in the index:")
print(result)

#Write a Python program to square the elements of a list using map() function. 
def square_num(n):
      return n * n
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))

#Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.
def change_case(s):
    return str(s).upper(), str(s).lower()

nums = {'a','i','e','f','s'}
print("original nums\n:",nums)
result = map(change_case,nums)
print(set(result))

#Write a Python program to add two given lists and find the difference between lists. Use map() function.
def addtional_substraction(x,y):
    return x+y, x-y
num1 = [10,20,304,05,50]
num2 = [20,39,44,34,23]
print("origianla list:\n")
print(num1)
print(num2)
result = map(addtional_substraction,num1,num2)
print("\nresult")
print(list(result))

#Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
nums_list = [1,2,3,4,5,6,6,7]
nums_tuple = [0,2,3,4,5,6,7]
print("original list and tuple:")
print(nums_list)
print(nums_tuple)
result_list = list(map(str,nums_list))
result_tuple = list(map(str,nums_tuple))
print(result_list)
print(result_tuple)

#Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer.
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
print("Original data:")
print(student_data)
students_data_name = list(map(lambda x:x[0], student_data))
students_data_dob = list(map(lambda x:x[1], student_data))
students_data_weight = list(map(lambda x:int(x[2][:-2]), student_data))
print("\nStudent name:")
print(students_data_name)
print("Student name:")
print(students_data_dob)
print("Student weight:")
print(students_data_weight)

#Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer.
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
print("Original data:")
print(student_data)
students_data_name = list(map(lambda x:x[0], student_data))
students_data_dob = list(map(lambda x:x[1], student_data))
students_data_weight = list(map(lambda x:int(x[2][:-2]), student_data))
print("\nStudent name:")
print(students_data_name)
print("Student name:")
print(students_data_dob)
print("Student weight:")
print(students_data_weight)


#Write a Python program to compute the square of first N Fibonacci numbers, using map function and generate a list of the numbers. 
import itertools
n = 10
def fibonacci_nums(x=0, y=1):
    yield x
    while True:
        yield y
        x, y = y, x + y
print("First 10 Fibonacci numbers:")
result = list(itertools.islice(fibonacci_nums(), n))
print(result)
square = lambda x: x * x 
print("\nAfter squaring said numbers of the list:")
print(list(map(square, result)))

#Write a Python program to compute the sum of elements of an given array of integers, use map() function. 
from array import array
def array_sum(nums_arr):
    sum_n = 0
    for n in nums_arr:
        sum_n += n
    return sum_n

nums = array('i', [1, 2, 3, 4, 5, -15])
print("Original array:",nums)
nums_arr = list(map(int, nums))
result = array_sum(nums_arr)
print("Sum of all elements of the said array:")
print(result)

#Write a Python program to find the ration of positive numbers, negative numbers and zeroes in an array of integers.
from array import array

def plusMinus(nums):
    n = len(nums)
    n1 = n2 = n3 = 0
    
    for x in nums:
        if x > 0:
            n1 += 1
        elif x < 0:
            n2 += 1
        else:
            n3 += 1
            
    return round(n1/n,2), round(n2/n,2), round(n3/n,2)

nums = array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
print("Original array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)
nums = array('i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
print("\nOriginal array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)
