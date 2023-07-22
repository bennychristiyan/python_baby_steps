import random
# parent class
class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):
        
        # setattr(x,y,z) ==> x.y = z; sets the value of specified attribute of the specified object  
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.rare = rare
        self.clean = clean
        self.heads = heads
        
        if self.rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        
        if self.clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour
        
    def __del__(self):
        print("Coin spent")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        return f"Rs.{int(self.original_value)} coin"

# inheritance
class _1Rupee(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "silver",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        # to access parent class
        super().__init__(**data)

class _2Rupee(Coin):
    def __init__(self):
        data = {
            "original_value": 2.00,
            "clean_colour": "silver",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 23.5,
            "thickness": 3.5,
            "mass": 12
        }
        # to access parent class
        super().__init__(**data)

class _5Rupee(Coin):
    def __init__(self):
        data = {
            "original_value": 5.00,
            "clean_colour": "gold",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 5,
            "mass": 15
        }
        # to access parent class
        super().__init__(**data)
    
class _10Rupee(Coin):
    def __init__(self):
        data = {
            "original_value": 10.00,
            "clean_colour": "silver_and_gold",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 27,
            "thickness": 4.15,
            "mass": 13
        }
        # to access parent class
        super().__init__(**data)
        


coins = [_1Rupee(), _2Rupee(), _5Rupee(), _10Rupee()]
for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.mass]
    string = "{}, Colour: {}, Value: {}, Diameter(mm): {}, Thickness(mm): {}, Num_edges: {}, Mass(g): {}".format(*arguments)
    print(string)

# output
"""

Rs.1 coin, Colour: silver, Value: 1.0, Diameter(mm): 22.5, Thickness(mm): 3.15, Num_edges: 1, Mass(g): 9.5
Rs.2 coin, Colour: silver, Value: 2.0, Diameter(mm): 23.5, Thickness(mm): 3.5, Num_edges: 1, Mass(g): 12
Rs.5 coin, Colour: gold, Value: 5.0, Diameter(mm): 22.5, Thickness(mm): 5, Num_edges: 1, Mass(g): 15
Rs.10 coin, Colour: silver_and_gold, Value: 10.0, Diameter(mm): 27, Thickness(mm): 4.15, Num_edges: 1, Mass(g): 13

"""