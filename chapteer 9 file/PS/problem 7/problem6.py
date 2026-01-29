# Write a program to find out the line number where python is present from ques 6.
with open("doc.log") as f:
    content = f.read().lower()
    

words= content.split()

for word in words:
    if "python" == word:
     print(f"its contain python :{word} ")