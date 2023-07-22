# two types of scope - global and local
# functions create local scope, whereas loops and if statements can't

# global scope
a = 100

def f1():
    print(a)
def f2():
    print(a)
f1()
f2()
print(a)

# local variable for only one function without global variable
def f1():
    a = 100
    print(a)
def f2():
    print(a)
f1()
f2()
print(a)

# local variable for all functions
a = 100
def f1():
    a = 100
    print(a)
def f2():
    a = 50
    print(a)
f1()
f2()
print(a)

# application of global and local variable
a = 100
def f1():
    b = a + 100
    print(b)
def f2():
    a = 50
    print(a)
f1()
f2()
print(a)

# changing global variable value within a function
a = 100
def f1():
    global a
    a = 250
    print(a)
def f2():
    a = 50
    print(a)
f1()
f2()
print(a)

# global variable with list
a = [1,2,3,4,5]
def f1():
    a = 100
    print(a)
def f2():
    a = 50
    print(a)
f1()
f2()
print(a)

# exception: dictionary and list single value can be changed without using global key inside a function
a = [1,2,3,4,5]
def f1():
    a[0] = 100
    print(a)
def f2():
    a = 50
    print(a)
f1()
f2()
print(a)




# output
"""

100
100
100
100
Traceback (most recent call last):
  File "c:\python_bible\functions\variable_scope.py", line 18, in <module>
    f2()
  File "c:\python_bible\functions\variable_scope.py", line 16, in f2
    print(a)
          ^
NameError: name 'a' is not defined
100
100
50
100
200
50
100
250
50
250
100
50
[1, 2, 3, 4, 5]
[100, 2, 3, 4, 5]
50
[100, 2, 3, 4, 5]

"""