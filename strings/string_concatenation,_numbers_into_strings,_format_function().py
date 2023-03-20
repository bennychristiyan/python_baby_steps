Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A = "part one"
>>> B = "part two"
>>> A + B
'part onepart two'
>>> A * 3
'part onepart onepart one'
>>> "=" * 20
'===================='
>>> print("TITLE")
TITLE
>>> "=" * 5
'====='
>>> C = 1
>>> A + C
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    A + C
TypeError: can only concatenate str (not "int") to str
>>> A + str(C)
'part one1'
>>> "{} - {}".format(A,C)
'part one - 1'
>>> "{1} - {0}".format(A,C)
'1 - part one'
