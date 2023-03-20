Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = "happy birthday"
x.index("birthday")
6
x.index("uahdiusgfibik")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x.index("uahdiusgfibik")
ValueError: substring not found
x.find("birthday")
6
x.find("khabvfikhsrb")
-1
x.index("Birthday")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.index("Birthday")
ValueError: substring not found
>>> x.find("Birthday")
-1
>>> y = "0000000happybirthday000000"
>>> y.strip("0")
'happybirthday'
>>> y.lstrip("0")
'happybirthday000000'
>>> y.rstrip("0")
'0000000happybirthday'
>>> z = input("what is ur name?:")
what is ur name?:benny  
>>> print(z)
benny  
>>> len(z)
7
>>> z = input("what is ur name?:")
what is ur name?:
>>> z = input("what is ur name?:").strip()
what is ur name?:benny       
>>> print(z)
benny
>>> len(z)
5
>>> #strip() removes the space on both ends
