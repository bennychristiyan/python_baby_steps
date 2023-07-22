# position of a value in a string (shows error if false)
x = "happy birthday"
print(x.index("birthday"))
print(x.index("uahdiusgfibik"))

# position of a value in a string (returns -1 if false)
print(x.find("birthday"))
print(x.find("khabvfikhsrb"))

# strip function (removes specific value)
y = "0000000happybirthday000000"
print(y.strip("0"))
print(y.lstrip("0"))
print(y.rstrip("0"))

# length of a string
z = input("what is your name?:")
print(z)
print(len(z))

# removes the space on both ends
print(z.strip())


# output
"""

6

Traceback (most recent call last):
  File "c:\python_bible\strings\cool_string_methods_2.py", line 4, in <module>
    print(x.index("uahdiusgfibik"))
          ^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: substring not found

6
-1
happybirthday
happybirthday000000
0000000happybirthday
what is your name?:Benny Christiyan
Benny Christiyan
16
Benny Christiyan

"""