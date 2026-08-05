#Typecasting is process of changing the datatype from one datatype  to another
#str() ,int(),float(),bool()
# in python we cannot change string to number
name = "ankitshrr"
age = "22"
gpa = 3.2
print("age:" ,type(age))
print("gpa:" ,type(gpa))
age = int(age)      # overwrite 
gpa = int(gpa)      # overwrite 
name= int(name)    #overwrite

print(type(age))
print(type(gpa))
print(type(name)) # Valueerror: real string cannot change to int
