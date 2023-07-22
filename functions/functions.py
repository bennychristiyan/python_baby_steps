# print and return are different as print doesn't store the value in a variable, whereas return does
def add (x,y):
    print(x + y)
a = add(10,5)
print(type(a))

def add (x,y):
    return x + y
a = add(10,5)
print(a)
print(type(a))

def rev(word):
    return word[::-1]
a = rev("benny")
print(a)
b = [1,2,3,4,5]
print(rev(b))

# output
"""

15
<class 'NoneType'>
15
<class 'int'>
ynneb
[5, 4, 3, 2, 1]

"""