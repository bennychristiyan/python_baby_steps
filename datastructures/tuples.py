# tuples () and strings are immutable, which means their value can't be changed
my_tuple = 1,2,3,4,5
print(my_tuple)
print(type(my_tuple))
my_tuple = (65,23,93,87,34)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0:3])

# lists are mutable
my_list = [6,34,86,234,56]
print(my_list)
my_list[2] = 100
print(my_list)

# strings are immutable, which means their value can't be changed
string = "Hello"
print(string)
string[2] = "a"
print(string)

# tuples are immutable
my_tuple = 1,2,3,4,5
print(my_tuple)
my_tuple[2] = 100
print(my_tuple) 

# changing list into tuple and tuple into list
my_list = tuple(my_list)
print(my_list)
my_list = list(my_list)
print(my_list)

# cool way of assigning value to tuple from tuple
A,B,C = (1,2,3)
print(A)
print(B)
print(C)
A,B,C = 1,2,3
print(A)
print(B)
print(C)
(A,B,C) = (1,2,3)
print(A)
print(B)
print(C)

# cool way of assigning value to tuple from list
D,E,F = [4,5,6]
print(D)
print(E)
print(F)

# cool way of assigning value to tuple from string
G,H,I = "789"
print(G)
print(H)
print(I)

# output
"""

(1, 2, 3, 4, 5)
<class 'tuple'>
(65, 23, 93, 87, 34)
<class 'tuple'>
(65, 23, 93)
[6, 34, 86, 234, 56]
[6, 34, 100, 234, 56]
Hello
Traceback (most recent call last):
  File "c:\python_bible\datastructures\tuples.py", line 17, in <module>
    string[2] = "a"
    ~~~~~~^^^
TypeError: 'str' object does not support item assignment
(1, 2, 3, 4, 5)
Traceback (most recent call last):
  File "c:\python_bible\datastructures\tuples.py", line 22, in <module>
    my_tuple[2] = 100
    ~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
(6, 34, 100, 234, 56)
[6, 34, 100, 234, 56]
1
2
3
1
2
3
1
2
3
4
5
6
7
8
9

"""