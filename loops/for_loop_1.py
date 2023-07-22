# for loop with range
for i in range(1,11):
    print(i)

# for loop with list
for i in [1,2,3,4,5]:
    print(i)

# for loop with string
for i in "abcde":
    print(i)

# for loop application
vowels = 0
consonants = 0
string = input("Enter a string: ").strip().lower()
for i in string:
    if i in "aeiou":
        vowels += 1
    elif i == " ":
        pass
    else:
        consonants += 1
print("The number of vowels are: ", vowels)
print("The number of consonants are: ", consonants)

# output
"""

1
2
3
4
5
6
7
8
9
10
1
2
3
4
5
a
b
c
d
e
Enter a string: bennychristiyan
The number of vowels are:  4
The number of consonants are:  11

"""