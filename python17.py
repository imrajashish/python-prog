#Write a Python program to convert an integer to a 2 byte Hex value
for i in range(1, 10):
    print(i,'-->',format(i, '#04x'))

#Write a Python program to compute Euclidean distance.
import math
# Example points in 3-dimensional space...
x = (5, 6, 7)
y = (8, 9, 9)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Euclidean distance from x to y: ",distance)

#Write a Python program to find perfect squares between two given numbers
def squares(a, b):
    lists=[]
    # Traverse through all numbers
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
print(squares(1, 30))
