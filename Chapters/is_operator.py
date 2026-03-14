#is checks whether two variables point to the same object in memory, not just if they have the same value.
a = [1,2,3]
b = [1,2,3]

print(a == b)  # True  (values are same)
print(a is b)  # False (different memory objects)
c = [1,2,3]
b = c

print(b is c)  # True (both point to same object)