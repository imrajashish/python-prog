#Write a Python program to calculate Euclid's totient function of a given integer. Use a primitive method to calculate Euclid's totient function. 
def gcd(p,q):
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)
print(phi_func(10))
print(phi_func(15))
print(phi_func(33))

#Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    
    else:
        return False;
print(test_distinct([1,5,7,9]))
print(test_distinct([1,5,7,7,9]))

#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))

#Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
def remove_nums(int_list):
    position = 3-1
    idx = 0
    len_list = (len(int_list))
    while len_list>0:
        idx = (position + idx)%len_list
        print(int_list.pop(idx))
        len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)

#Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.
def three_sum(nums):
      result = []
  nums.sort()
  for i in range(len(nums)-2):
    if i> 0 and nums[i] == nums[i-1]:
      continue
    l, r = i+1, len(nums)-1
    while l < r:
      s = nums[i] + nums[l] + nums[r]
      if s > 0:
        r -= 1
      elif s < 0:
          l += 1
      else:
        # found three sum
        result.append((nums[i], nums[l], nums[r]))
        # remove duplicates
        while l < r and nums[l] == nums[l+1]:
          l+=1
          while l < r and nums[r] == nums[r-1]:
            r -= 1
            l += 1
            r -= 1
          return result

x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
print(three_sum(x))
