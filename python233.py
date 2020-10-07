#Write a Python program to read each row from a given csv file and print a list of strings.
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

#Write a Python program to read a given CSV file as a list.
import csv
with open('employees.csv', newline='') as f:
   reader = csv.reader(f)
   data_list = list(reader)
print(data_list)
