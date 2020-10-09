#Write a Python program to append text to a file and display the text.
import csv
with open('departments.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar='|')
 for row in data:
   print(', '.join(row))

#Write a Python program to read a given CSV file having tab delimiter.
import csv
with open('countries.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter = '\t')
 for row in data:
   print(', '.join(row))

#Write a Python program to read a given CSV file having tab delimiter.
import csv
with open('countries.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter = '\t')
 for row in data:
   print(', '.join(row))
