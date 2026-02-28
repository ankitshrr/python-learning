# Write a program to make a copy of a text file “this. txt”

with open("this.txt")  as f:
    content= f.read()



with open("new.txt","w") as f:
        new= f.write(content)