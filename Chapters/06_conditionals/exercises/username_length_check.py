# Write a program to find whether a given username contains less than 10  characters or not.
char = input("enter the username:")
if len(char) >10:
    print(f"username contain  more than {char}")
elif len(char)<=10:
    print(f"character  less than {char}")
    