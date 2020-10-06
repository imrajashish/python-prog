#Write a Python program that iterate over elements repeating each as many times as its count.
from collections import Counter
c = Counter(p=4, q=2, r=0, s=-2)
print(list(c.elements()))

#Write a Python program to find the most common elements and their counts of a specified text.
from collections import Counter
s = 'lkseropewdssafsdfafkpwe'
print("Original string: "+s)
print("Most common three characters of the said string:")
print(Counter(s).most_common(3))
