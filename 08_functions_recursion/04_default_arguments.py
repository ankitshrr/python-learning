# This code demonstrates the behavior of default mutable arguments in Python.
def func(val, lst=[]):
    lst.append(val)
    return lst


print(func(1))
print(func(2))
print(func(3))