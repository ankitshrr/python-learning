name = ["ankit","ankita","santosh"]
search = input("enter the check to check the list whether it is in list or not:")

if (search in name):
    print(f"it is in list: {search}")
else:
    print(f"it is not in list: {search}")