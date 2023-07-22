# adding an integer to the list
A = [5,23,65,87,23]
print(A)
A = A + 1
print(A)
A = A + [1]
print(A)

# adding a string to the list
A = A + "BCD"
print(A)
A = A + ["BCD"]
print(A)

# list function
A = A + list("BCD")
print(A)
A = A + list(123)
print(A)
# can also be typed as list(str(123))
A = A + list("123")
print(A)

# adding list to list
A = [5,23,65,87,23]
print(A)
A = A + [2,43,76,23]
print(A)
A = A + [[4,25,75,23]]
print(A)

# append function
A.append([6,256,234,876,45])
print(A)
A = A.append(10)
print(A)
print(type(A))

# insert function (insert(index number, value))
A = [5,23,65,87,23]
print(A)
A.insert(2,554)
print(A)
A.insert(2,[3,763,79])
print(A)
A = A.insert(2,54)
print(A)

# remove function
A = [5,23,65,87,23]
print(A)
A.remove(23)
print(A)
A.remove(87)
print(A)

# output
"""

[5, 23, 65, 87, 23]
Traceback (most recent call last):
  File "c:\python_bible\datastructures\more_ways_to_add_items_to_list.py", line 3, in <module>
    A = A + 1
        ~~^~~
TypeError: can only concatenate list (not "int") to list
[5, 23, 65, 87, 23, 1]
Traceback (most recent call last):
  File "c:\python_bible\datastructures\more_ways_to_add_items_to_list.py", line 7, in <module>
    A = A + "BCD"
        ~~^~~~~~~
TypeError: can only concatenate list (not "str") to list
[5, 23, 65, 87, 23, 1, 'BCD']
[5, 23, 65, 87, 23, 1, 'BCD', 'B', 'C', 'D']
Traceback (most recent call last):
  File "c:\python_bible\datastructures\more_ways_to_add_items_to_list.py", line 13, in <module>
    A = A + list(123)
            ^^^^^^^^^
TypeError: 'int' object is not iterable
[5, 23, 65, 87, 23, 1, 'BCD', 'B', 'C', 'D', '1', '2', '3']
[5, 23, 65, 87, 23]
[5, 23, 65, 87, 23, 2, 43, 76, 23]
[5, 23, 65, 87, 23, 2, 43, 76, 23, [4, 25, 75, 23]]
[5, 23, 65, 87, 23, 2, 43, 76, 23, [4, 25, 75, 23], [6, 256, 234, 876, 45]]
None
<class 'NoneType'>
[5, 23, 65, 87, 23]
[5, 23, 554, 65, 87, 23]
[5, 23, [3, 763, 79], 554, 65, 87, 23]
None
[5, 23, 65, 87, 23]
[5, 65, 87, 23]
[5, 65, 23]

"""