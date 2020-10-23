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

# Write a Python program to create a new deque with three items and iterate over the deque's elements.
from collections import deque
dq = deque('aeiou')
for elements in dq:
    print(elements)

#Write a Python program to find the occurrences of 10 most common words in a given text.
from collections import Counter
import re
text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""
words = re.findall('\w+',text)
print(Counter(words).most_common(10))


#Write a Python program that accept name of given subject and marks. Input number of subjects in first line and subject name,marks separated by a space in next line. Print subject name and marks in order of its first occurrence
import collections, re
n = int(input("Number of subjects: "))
item_order = collections.OrderedDict()
for i in range(n):
   sub_marks_list = re.split(r'(\d+)$',input("Input Subject name and marks: ").strip())
   subject_name = sub_marks_list[0]
   item_price = int(sub_marks_list[1])
   if subject_name not in item_order:
       item_order[subject_name]=item_price
   else:
       item_order[subject_name]=item_order[subject_name]+item_price
           
for i in item_order:
   print(i+str(item_order[i]))

#Write a Python program that accept some words and count the number of distinct words. Print the number of distinct words and number of occurrences for each distinct word according to their appearance.
from collections import Counter, OrderedDict
class OrderedCounter(Counter,OrderedDict):
   pass
word_array = []
n = int(input("Input number of words: "))
print("Input the words: ")
for i in range(n):
   word_array.append(input().strip())
word_ctr = OrderedCounter(word_array)
print(len(word_ctr))
for word in word_ctr:
   print(word_ctr[word])
