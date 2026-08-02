# A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
p1= "Make a lot of money"
p2= "buy now"
p3= "subscribe this"
p4= "click this"
message = input("enter the message to detect spam")
if  p1 == message or p2 == message or p3 == message or p4 == message:
    print(f"spam detected: {message}")
else  :
    print("not a spam")