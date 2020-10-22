#elif
x=int(input("Enter the number: "))
if x == 1:
    print("one")
elif x ==2:
    print("Two")
elif x ==3:
    print("Three")
elif x ==4:
    print("Four")
elif x ==5:
    print("Five")
else:
    print("wrong input")

#for
x = ['A',4,43]
for i in x:
    print(x[2])

for i in range(10):
    print(i)

#break
av = 5
x = int(input("Enter the number:"))
i = 1
while i <= x:
    if i>av:
        print("out of stack")
        break
    print("Candny")
    i+=1
    print("bye")

#continue
for i in range(1,101):
    if i%3 ==0 | i%5 ==0:
        continue
    print(i)

#pass
for i in range(1,101):
    if (i%2 !=0):
        pass
    else:
        print(i)

#for else
nums = [12,23,43,5,4,55,56]
for num in nums:
    if num%5 == 0:
        print(num)
        break
    else:
        print("not defined")

#matrix
from numpy import *
m = matrix('123;654;1.63')
print(m)

#function
def greet():
    print("Hello")
    print("good morning")
greet()
greet()
greet()

#function
def add(x,y):
    c = x+y
    print(c)
add(2,43)

#function argument
def update(x):
    x= 6
    print("x",x)
    a = 10
    update(a)
    print("a",a)
#keyword variable
def person(name,**data):
    print(name)
    print(data)
person('ashish',age= 32,city = "patna")

#fibonacchi series
def fact(n):
    if n == 0:
        return 1
        return n*fact(n-1)
        result = fact(5)
    print(result)