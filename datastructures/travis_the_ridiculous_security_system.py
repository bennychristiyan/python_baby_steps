known_users = ["George", "Merlin", "Deborah", "Hannah", "Harry", "Johnny", "Mark", "Matthew"]
print(len(known_users))
while True:
    print("Hi! My name is Travis")
    name = input("What is your name: ").strip().capitalize()
    if name in known_users:
        # can also be typed as print("Hello {}".format(name))
        print(f"Hello {name}!")
        remove = input("Would you like to be removed from the system (y/n): ").strip().lower()
        if remove == "y":
            print(known_users)
            # to delete a specific index value del function is used. eg: del known_users[0], deletes the 1st name in the list. 
            # Slice can also be used. eg: del known_users[0:2], deletes the 1st two names 
            # .pop() can be used to remove a specific index value. eg: known_users.pop(2), deletes the 3rd name in the list
            # remove function is used to remove the items from the list
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No problem! I didn't want you to leave anyway")
        else:
            print("Invalid option")
    else:
        print(f"Hmmm, I don't think I have met you yet {name}")
        add = input("Would you like to be added to the system (y/n): ").strip().lower()
        if add == "y":
            print(known_users)
            # append function is used to add items to the list
            known_users.append(name)
            print(known_users)
        elif add == "n":
            print("No worries! See you around")
        else:
            print("Invalid option")

# output
"""

Hi! My name is Travis
What is your name: hannah
Hello Hannah!
Would you like to be removed from the system (y/n): y
['George', 'Merlin', 'Deborah', 'Hannah', 'Harry', 'Johnny', 'Mark', 'Matthew']
['George', 'Merlin', 'Deborah', 'Harry', 'Johnny', 'Mark', 'Matthew']

Hi! My name is Travis
What is your name: george
Hello George!
Would you like to be removed from the system (y/n): n
No problem! I didn't want you to leave anyway

Hi! My name is Travis
What is your name: benny
Hmmm, I don't think I have met you yet Benny
Would you like to be added to the system (y/n): y
['George', 'Merlin', 'Deborah', 'Harry', 'Johnny', 'Mark', 'Matthew']
['George', 'Merlin', 'Deborah', 'Harry', 'Johnny', 'Mark', 'Matthew', 'Benny']


Hi! My name is Travis
What is your name: benny
Hello Benny!
Would you like to be removed from the system (y/n): n
No problem! I didn't want you to leave anyway

Hi! My name is Travis
What is your name: vendetta
Hmmm, I don't think I have met you yet Vendetta
Would you like to be added to the system (y/n): n
No worries! See you around

Hi! My name is Travis
What is your name: alice
Hmmm, I don't think I have met you yet Alice
Would you like to be added to the system (y/n): t
Invalid option

"""