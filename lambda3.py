#Write a Python program to find intersection of two given arrays using Lambda
num1 = [1,2,3,4,5,6,7,8,7]
num2 = [3,4,5,6,6,8,8,9,8,7]
print("\n original arrays:")
print(num1)
print(num2)
result = list(filter(lambda x: x in num1,num2))
print("\n Intersection of the said array: ",result)

#Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
num1 = [12,23,43,54,5,-2,-3,-4,-3232]
print("\n original array: ")
print(num1)
result = [x for x in num1 if x<0] + [x for x in num1 if x>0]
print(result)

#Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
array_nums = [1,2,3,4,5,67,76,678,78,789,989,90,-1]
print("\n original array: ")
print(array_nums)
odd_ctr = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
even_ctr = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
print(odd_ctr)
print(even_ctr)

# Write a Python program to find the values of length six in a given list using Lambda. 
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
  print(d)

#Write a Python program to add two given lists using map and lambda.
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print("Original list:")
print(nums1)
print(nums2)
result = map(lambda x, y: x + y, nums1, nums2)
print("\nResult: after adding two list")
print(list(result))

#Write a Python program to find the second lowest grade of any student(s) from the given names and grades of each student using lists and lambda. Input number of students, names and grades of each student. 
students = []
sec_name = []
second_low = 0
n = int(input("Input number of students: "))
for _ in range(n):
   s_name = input("Name: ")
   score = float(input("Grade: "))
   students.append([s_name,score])
print("\nNames and Grades of all students:")
print(students)
order =sorted(students, key = lambda x: int(x[1]))
for i in range(n):
   if order[i][1] != order[0][1]:
       second_low = order[i][1]
       break
print("\nSecond lowest grade: ",second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nNames:")
for s_name in sec_student_name:
   print(s_name)
