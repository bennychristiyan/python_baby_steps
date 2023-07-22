import random 
class Coin:

    # class methods
    # constructor # initialize object's attributes
    def __init__(self, rare = False):
        self.rare = rare
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True
    
    def rust(self):
        self.colour = "brownish"
    
    def clean(self):
        self.colour = "gold"
    
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
    
    # destructor
    def __del__(self):
        print("Coin spent")

coin1 = Coin(rare = True)
coin2 = Coin()
print(coin1.rare)
print(coin2.rare)
print(coin1.value)
print(coin2.value)
coin1.rust()
print(coin1.colour)
print(coin2.colour)
coin1.clean()
print(coin1.colour)
coin1.flip()
print(coin1.heads)
coin1.flip()
print(coin1.heads)
del coin1
del coin2
coin1
coin2

# output
"""
True
False
1.25
1.0
brownish
gold
gold
False
False
Coin spent
Coin spent
Traceback (most recent call last):
  File "c:\python_bible\OOPs_(Object_Oriented_Programming)\make_a_coin_2.py", line 46, in <module>
    coin1
NameError: name 'coin1' is not defined
Traceback (most recent call last):
  File "c:\python_bible\OOPs_(Object_Oriented_Programming)\make_a_coin_2.py", line 46, in <module>
    coin2
NameError: name 'coin2' is not defined

"""