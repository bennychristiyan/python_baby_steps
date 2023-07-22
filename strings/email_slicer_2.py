word = "the weather is so nice today"

# printing a value from a string using reverse count index number
print(word[-1])
print(word[-2])
print(word[-14])

# printing index number of a value from a string
print(word.index("weather"))
print(word.index("today"))

# printing a value from a string using intervals using values from the string
print(word[word.index("weather"):word.index("today")])
print(word[word.index("weather"):word.index("o")])

# output
"""

y
a

4
23
weather is so nice
weather is s

"""