Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"hello".count("e")
1
x = "Happy birthday"
x.count("day")
1
x.upper()
'HAPPY BIRTHDAY'
x.lower()
'happy birthday'
x = x.lower()
x
'happy birthday'
x.capitalize()
'Happy birthday'
x.title()
'Happy Birthday'
x = x.title()
x
'Happy Birthday'
x.isupper()
False
x.islower()
False
>>> x.iscapitalize()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x.iscapitalize()
AttributeError: 'str' object has no attribute 'iscapitalize'. Did you mean: 'capitalize'?
>>> x.istitle()
True
>>> x.isalpha()
False
>>> "HappyBirthday".isalpha()
True
>>> "123".isdigit()
True
>>> x.isdigit()
False
>>> x.isalnum()
False
>>> "happybirthday123".isalnum()
True
>>> "happy birthday1234".isalnum()
False



