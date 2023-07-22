# function with 3 parameters
def about(name, age, likes):
    sentence = f"Meet {name}! They are {age} years old and they like {likes}"
    return sentence
# positional arguments
a = about("benny", 18, "python")
print(a)

# keyword arguments
b = about(age = 18, likes = "nature", name = "luffy")
print(b)

# missing an argument
"""c = about("benny", 18)
print(c)"""

# default value for a parameter
def about(name, age, likes = "anime"):
    sentence = f"Meet {name}! They are {age} years old and they like {likes}"
    return sentence
d = about("jack", 23)
print(d)
# changing the default value of the parameter
e = about("sanji", 25, "cook")
print(e)

# default value parameters must start from the end (or) last
"""def about(name, age = 25, likes):
    sentence = f"Meet {name}! They are {age} years old and they like {likes}"
    return sentence
f = about("jack", 23)
print(f)"""
def about(name, age = 25, likes = "one piece"):
    sentence = f"Meet {name}! They are {age} years old and they like {likes}"
    return sentence
f = about("jack", 23)
print(f)

# default value parameters without any arguments
def about(name = "zoro", age = 25, likes = "one piece"):
    sentence = f"Meet {name}! They are {age} years old and they like {likes}"
    return sentence
f = about()
print(f)

# output
"""

Meet benny! They are 18 years old and they like python
Meet luffy! They are 18 years old and they like nature
Traceback (most recent call last):
  File "c:\python_bible\functions\keyword_arguments_ and_default_parameters.py", line 13, in <module>
    c = about("benny", 18)
        ^^^^^^^^^^^^^^^^^^
TypeError: about() missing 1 required positional argument: 'likes'
Meet jack! They are 23 years old and they like python
Meet sanji! They are 25 years old and they like cook
  File "c:\python_bible\functions\keyword_arguments_ and_default_parameters.py", line 18
    def about(name, age = 25, likes):
                              ^^^^^
SyntaxError: non-default argument follows default argument
Meet jack! They are 23 years old and they like one piece
Meet zoro! They are 25 years old and they like one piece

"""