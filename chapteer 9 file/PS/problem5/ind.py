# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.   Repeat program 4 for a list of such words to be censored.

censored= ["donkey","monkey","tonkey"]
with open("doc.txt") as f :
    content = f.read()

    for word in censored:
        content = content.replace(word, "######")

with open("doc.txt","w") as f :
    f.write(content)