A = "part one"
B = "part two"
C = 1

# concatenation
print(A + B)
print(A * 3)
print("=" * 20)
print("TITLE")
print("=" * 5)
print(A + C)

# numbers into strings
print(A + str(C))

# format function
print("{} - {}".format(A,C))
print("{1} - {0}".format(A,C))

#output
"""

part onepart two
part onepart onepart one
====================
TITLE
=====

Traceback (most recent call last):
  File "c:\python_bible\strings\string_concatenation,_numbers_into_strings,_format_function().py", line 9, in <module>        
    print(A + C)
          ~~^~~
TypeError: can only concatenate str (not "int") to str

part one1
part one - 1
1 - part one

"""