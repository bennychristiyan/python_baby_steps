# list comprehension in digits
even_numbers = [x for x in range(1,51) if x % 2 == 0]
print(even_numbers)
odd_numbers = [x for x in range(1,51) if x % 2 != 0]
print(odd_numbers)

# list comprehension in strings
words = ["the", "quick", "fox", "jumps"]
answers = [[w.upper(), w.lower(), len(w)] for w in words]
print(answers)

# output
"""

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
[['THE', 'the', 3], ['QUICK', 'quick', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5]]

"""