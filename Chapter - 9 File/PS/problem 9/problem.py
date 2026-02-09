# Write a program to find out whether a file is identical & matches the content of another file.
with open("doc1.log") as f:
    content = f.read()

with open("doc.log") as f:
    content1 = f.read()

if content1 == content: 
    print("its contain same file")
else:
    print("it doesnt contain same file")





