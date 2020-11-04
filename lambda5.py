#Write a Python program that multiply each number of given list with a given number using lambda function. Print the result.
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

#Write a Python program that sum the length of the names of a given list of names after removing the names that starts with an lowercase letter. Use lambda function
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
print("Result:")
print(len(''.join(sample_names)))

#Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print("Original list:",nums)

total_negative_nums = list(filter(lambda nums:nums<0,nums))
total_positive_nums = list(filter(lambda nums:nums>0,nums))

print("Sum of the positive numbers: ",sum(total_negative_nums))
print("Sum of the negative numbers: ",sum(total_positive_nums))

# Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.
def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
print(divisible_by_digits(1,22))

#Write a Python program to create the next bigger number by rearranging the digits of a given number.
def rearrange_bigger(n):
    #Break the number into digits and store in a list
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
n = 12
print("Original number:",n)
print("Next bigger number:",rearrange_bigger(n))

n = 10
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
      
n = 201
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 102
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 445
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
