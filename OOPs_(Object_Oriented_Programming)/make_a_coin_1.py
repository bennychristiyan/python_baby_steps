class Coin:

    # class states
    value = 1.00
    colour = "gold"
    num_edges = 1
    diameter = 22.5 #mm
    thickness = 3.15 #mm
    heads = True

coin1 = Coin()
print(type(coin1))
print(coin1.value)
print(coin1.colour)

# after rusting it turns brownish
coin1.colour = "brownish"
print(coin1.colour)

# the objects can have unique characters, but the class is common to all and doesn't change
coin2 = Coin()
print(coin2.colour)

# output
"""

<class '__main__.Pound'>
1.0
gold
brownish
gold

"""