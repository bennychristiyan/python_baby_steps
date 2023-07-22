A = 10
B = 20

# not operator (gives opposite of the Boolean value)
print(not False)
print(not True)
print(not A < B)
print(not A >= B)

# and operator (True only if both values are True)
print(True and False)
print(A < B and B > A)
print(A > B and B > A)

# or operator (True even if only one value is True)
print(True or False)
print(A < B or B > A)
print(A == B or B > A)

# logical operators combined in if statement
if not((A > B and B > A) or (A == B and B != A)):
    print("It is true")

# output
"""

True
False
False
True
False
True
False
True
True
True
It is true

"""