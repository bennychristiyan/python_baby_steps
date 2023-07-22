# lists [] are mutable, which means their values can be changed
my_list = [1,2,3,4,5]
print(my_list)
print(type(my_list))
print(my_list[1])
print(my_list[-1])

# single element can be stored in a variable
x = my_list[0]
print(x)

# list can contain all types of datastructures
my_list = [1,2,3,"a","b","c",True,False]
print(my_list)
print(my_list[-1])
print(my_list[4])

# list can contain lists
my_list = [[1,2,"c"],["a","b",3],[True,False,"d"]]
print(my_list)
print(my_list[2])
print(my_list[-2])
print(my_list[1][2])
print(my_list[0][-1])

# output
"""

[1, 2, 3, 4, 5]
<class 'list'>
2
5
1
[1, 2, 3, 'a', 'b', 'c', True, False]
False
b
[[1, 2, 'c'], ['a', 'b', 3], [True, False, 'd']]
[True, False, 'd']
['a', 'b', 3]
3
c

"""