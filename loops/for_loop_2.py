# for loop with dictionary
students = {
    "Male":["Bob", "Dan", "John", "Matthew"],
    "Female":["Elizabeth", "Esdeath", "Robin", "Robin"]
}
for i in students.keys():
    for j in students[i]:
        if "a" in j:
            print(j)

# output
"""

Dan
Matthew
Elizabeth
Esdeath

"""