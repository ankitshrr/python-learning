#Write a program to mine a log file and find out whether it contains ‘python’. 

with open("doc.log") as f:
    content = f.read()
    
# if "python" in content:
#     print(f"its contain python {content}")

words= content.split()

for word in words:
    if "python" == word:
     print(f"its contain python :{word,content.count("python")} ")