# list inside a dictionary
students = {
    "Alice": ["ID001", 23, "A"], 
    "Bob": ["ID002", 32, "B"], 
    "Claire": ["ID003", 28, "C"], 
    "Dan": ["ID004", 27, "D"], 
    "Emma": ["ID005", 25, "E"]
    }
print(students["Claire"])
print(students["Claire"][1])
print(students["Dan"][1:])

# dictionary inside a dictionary
students = {
    "Alice": {"id":"ID001", "age":23, "grade":"A"}, 
    "Bob": {"id":"ID002", "age":32, "grade":"B"}, 
    "Claire": {"id":"ID003", "age":28, "grade":"C"}, 
    "Dan": {"id":"ID004", "age":27, "grade":"D"}, 
    "Emma": {"id":"ID005", "age":25, "grade":"E"}
    }
print(students["Emma"]["age"])
print(students["Bob"]["id"], students["Bob"]["grade"])

# output
"""

['ID003', 28, 'C']
28
[27, 'D']
25
ID002 B

"""