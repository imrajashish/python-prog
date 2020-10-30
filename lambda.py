#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))

#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def func_compute(n):
     return lambda x : x * n
result = func_compute(2)
print("Double the number of 15 =", result(15))
result = func_compute(3)
print("Triple the number of 15 =", result(15))
result = func_compute(4)
print("Quadruple the number of 15 =", result(15))
result = func_compute(5)
print("Quintuple the number 15 =", result(15))
