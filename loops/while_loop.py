# while loop works only for true condition
while True:
    print("Hello")
while 2>1:
    print("Hello")

# while loop returns an empty space for the false condition
while False:
    print("Hello")

# printing numbers from 1 to 10
number = 1
while number <= 10:
    print(number)
    number = number + 1

# printing even numbers from 1 to 20
number = 1
while number <= 20:
    if number % 2 == 0:
        print(number)
    number = number + 1

# printing odd numbers from 1 to 20
number = 1
while number <= 20:
    if number % 2 != 0:
        print(number)
    number = number + 1

# appending values to a list
List = []
while len(List) < 3:
    name = input("Please, enter the name: ").strip().title()
    List.append(name)
print(List)
print("The list is full")


# output
"""

Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
.
.
.
.
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
.
.
.
.

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
2
4
6
8
10
12
14
16
18
20
1
3
5
7
9
11
13
15
17
19
Please, enter the name: bob    
Please, enter the name: claire
Please, enter the name: emma
['Bob', 'Claire', 'Emma']
The list is full

"""