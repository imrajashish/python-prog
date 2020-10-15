#Write a Python program to find the class wise roll number from a tuple-of-tuples.
from collections import defaultdict
classes = (
    ('v',1),
    ('v1',2),
    ('v3',3)
)
class_roll_no = defaultdict(list)
for class_name,roll_id in classes:
    class_roll_no[class_name].append(roll_id)
print(class_roll_no)

#Write a Python program to count the number of students of individual class.
from collections import Counter
classes = (
('V', 1),
('VI', 1),
('V', 2),
('VI', 2),
('VI', 3),
('VII', 1),
)
students = Counter(class_name for class_name, no_students in classes)
print(students)

#Write a Python program to get the unique enumeration values.
import enum
class states(enum.Enum):
    Bihar = 10
    odish = 20
    bangale = 40
    delhi = 50
    up = 60
for result in states:
    print('{:15} = {}'.format(result.name, result.value))

#Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order.
from collections import OrderedDict
dict = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
new_dict = OrderedDict(dict.items())
for key in new_dict:
    print(key,new_dict[key])
print("\nIn revese order: ")
for key in reversed(new_dict):
    print(key,new_dict[key])

#Write a Python program to group a sequence of key-value pairs into a dictionary of lists.
from collections import defaultdict
class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
d = defaultdict(list)
for k, v in class_roll:
    d[k].append(v)
print(sorted(d.items()))
