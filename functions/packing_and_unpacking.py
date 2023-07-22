# *args
# unpacking any iterable datatype (one * for normal arguments)
print(1,2,3,4,5)
numbers = [1,2,3,4,5]
print(numbers)
print(*numbers)

print("a", "b", "c", "d", "e")
letters = "abcde"
print(letters)
print(*letters)

# packing any iterable data type (one * for normal arguments)
def add(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
a = add(1,2,3,4,5,6,7,8,9)  
print(a)

# **kwargs
# unpacking a dictionary (two ** for keyword arguments)
def about(name, age, likes):
    sentence = f"Meet {name}! They are {age} years old and they like {likes}"
    return sentence
dictionary = {"name":"usopp", "age":20, "likes":"fight"}
a = about(**dictionary)
print(a)
dictionary = { "age":50, "name":"brook", "likes":"sword"}
a = about(**dictionary)
print(a)

# packing a dictionary (two ** for keyword arguments)
def goku(**kwargs):
    for keys , values in kwargs.items():
        print(f"{keys}:{values}")
goku(nami = "female", chopper = "male")

# output
"""

1 2 3 4 5
[1, 2, 3, 4, 5]
1 2 3 4 5
a b c d e
abcde
a b c d e
45
Meet usopp! They are 20 years old and they like fight
Meet brook! They are 50 years old and they like sword
nami:female
chopper:male

"""