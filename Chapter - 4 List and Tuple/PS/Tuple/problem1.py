# Check that a tuple type cannot be changed in python.
chek = (121,32,232232)
result = str(chek) #changing tuple to str datatype
print(type(result)) 
print(type(chek))
print(type(chek[0]))