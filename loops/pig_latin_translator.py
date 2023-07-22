# get sentence from the user
original = input("Enter a sentence: ").strip().lower()

# split sentence into words
words = original.split()

# loop through words and convert into pig latin
new_words = []
for i in words:
    # if the word starts with a vowel
    if i[0] in "aeiou":
        new_word = i + "yay"
        new_words.append(new_word)
    # if the word starts with a consonant
    else:
        vowel_position = 0
        for j in i:
            if j not in "aeiou":
                vowel_position += 1
            else:
                break
        consonants = i[:vowel_position]
        the_rest = i[vowel_position:]
        new_word = the_rest + consonants + "ay"
        new_words.append(new_word)

# stick the words back together
output = " ".join(new_words)

# output the final string
print(output)

# output
"""

Enter a sentence: he is an honest man 
ehay isyay anyay onesthay anmay

"""