#Combine multiple lists together.

names = ["Ankit", "Ram"]
ages = [20, 21]
job=["code", "data scientist"]

for name,age,job in zip(names, ages,job):
    print(name, age,job)
