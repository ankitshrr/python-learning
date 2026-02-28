#  Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 
class program :
     a = "ankit"

ankit = program()
ankit.a=0 
print(ankit.a)

print(program.a)

