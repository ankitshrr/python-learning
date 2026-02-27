#In Python, how can you take multiple inputs from the user in one line?
a, b = map(int, input("Enter two numbers: ").split())
print(a + b)