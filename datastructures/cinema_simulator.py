films = {
    "Finding Dory":[3,10],
    "Tarzan":[5,10],
    "Little Mermaid":[4,10],
    "Narnia":[10,15],
    "Harry Potter":[15,1]
}
while True:
    # asking the choice of film
    choice = input("What film would you like to watch: ").strip().title()
    if choice in films:
        # asking the age
        age = int(input("How old are you: ").strip())
        if age >= films[choice][0]:
            # determining if there are seats available
            num_of_seats = films[choice][1]
            if num_of_seats > 0:
                print("Please, enjoy the film")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we're sold out!")
        else:
            print("Sorry, you are too young to watch that film")
    else:
        print("Sorry, the requested film is currently unavailable")

# output
"""

What film would you like to watch: harry potter
How old are you: 26
Please, enjoy the film

What film would you like to watch: harry potter
How old are you: 54
Sorry, we're sold out!

What film would you like to watch: narnia
How old are you: 9
Sorry, you are too young to watch that film

What film would you like to watch: one piece
Sorry, the requested film is currently unavailable

"""