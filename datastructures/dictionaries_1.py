# dictionaries {key:value} are mutable and they don't necessarily prints in same order and sets {} are mutable
students = {"Alice":23, "Bob":32, "Claire":28, "Dan":27, "Emma":25}
print(students)
print(students["Dan"])

# adding a new key and value
students["Fred"] = 22
print(students)
print(students["Fred"])

# changing the value of a key
students["Alice"] = 24
print(students["Alice"])

# deleting a key
del students["Fred"]
print(students)
print(students["Fred"])

# printing keys, values and all items
print(students.keys())
print(students.values())
print(students.items())

# dictionaries doesn't support indexing
print(students.keys()[0])

# converting the dictionary into a list
a = list(students.keys())
print(a)
print(a[0])
print(a[1])
print(list(students.values())[2:])

# output
"""

{'Alice': 23, 'Bob': 32, 'Claire': 28, 'Dan': 27, 'Emma': 25}
27
{'Alice': 23, 'Bob': 32, 'Claire': 28, 'Dan': 27, 'Emma': 25, 'Fred': 22}
22
24
{'Alice': 24, 'Bob': 32, 'Claire': 28, 'Dan': 27, 'Emma': 25}
Traceback (most recent call last):
  File "c:\python_bible\datastructures\dictionaries.py", line 12, in <module>
    print(students["Fred"])
          ~~~~~~~~^^^^^^^^
KeyError: 'Fred'
dict_keys(['Alice', 'Bob', 'Claire', 'Dan', 'Emma'])
dict_values([24, 32, 28, 27, 25])
dict_items([('Alice', 24), ('Bob', 32), ('Claire', 28), ('Dan', 27), ('Emma', 25)])
Traceback (most recent call last):
  File "c:\python_bible\datastructures\dictionaries.py", line 17, in <module>
    print(students.keys()[0])
          ~~~~~~~~~~~~~~~^^^
TypeError: 'dict_keys' object is not subscriptable
['Alice', 'Bob', 'Claire', 'Dan', 'Emma']
Alice
Bob
[28, 27, 25]

"""