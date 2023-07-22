# number of times a value appears in a string
print("hello".count("e"))
x = "Happy birthday"
print(x.count("day"))

# making all letters uppercase 
print(x.upper())

# making all letters lowercase
print(x.lower())

# making 1st letter of 1st word capital
print(x.capitalize())

# making 1st letter of all words capital 
print(x.title())

# checking whether all letters are uppercase 
print(x.isupper())

# checking whether all letters are lowercase
print(x.islower())

# checking whether 1st letter of all words are capital
print(x.istitle())

# checking whether the string is only letters
print(x.isalpha())
print("HappyBirthday".isalpha())

# checking whether the string is only numbers
print("123".isdigit())
print(x.isdigit())

# checking whether the string is only letters and numbers
print(x.isalnum())
print("happybirthday123".isalnum())
print("happy birthday1234".isalnum())

# output
"""

1
1
HAPPY BIRTHDAY
happy birthday
Happy birthday
Happy Birthday
False
False
False
False
True
True
False
False
True
False

"""

