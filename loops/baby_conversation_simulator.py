from random import choice
questions = ["Why the sky is blue?: ", "Why the sun is so far away?: ", "why did dianosaurs disappear?: "]
answer = input(choice(questions)).strip().lower()
while answer != "just because":
    answer = input("why?: ").strip().lower()
print("Oh...Okay")

# output
"""

Why the sky is blue?: because of the light that passes through the atmosphere
why?: wavelength
why?: just because
Oh...Okay
Why the sun is so far away?: just because
Oh...Okay
why did dianosaurs disappear?: i don't know
why?: just because
Oh...Okay

"""