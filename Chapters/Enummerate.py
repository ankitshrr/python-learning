# Enumerate is a built-in function in Python that allows you to loop through an iterable and have an automatic counter. It returns both the index and the value of each item in the iterable.
names = ["Ankit", "Ram", "Shyam"]

for index, name in enumerate(names):
    print(index, name)