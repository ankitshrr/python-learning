import copy

a = [[1,2], [3,4]]
b = a.copy()         # shallow
c = copy.deepcopy(a) # deep
print(c)
print(b)