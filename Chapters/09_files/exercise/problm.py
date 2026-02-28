#A file contains a word “Donkey” multiple times. You need to write a program   which replace this word with ##### by updating the same file.
with open("doc.txt","r") as f:
    contain=f.read()

rep = contain.replace("donkey","######")

with open("doc.txt","w") as f:
    f.write(rep)
    
