# l = ["harry","sohan","shres","rahul"]

# for name in l :
#     if name[0] == "s":
#         print(f"hello, {name}")

l = ["harry","sohan","shres","rahul"]

i = 0
while i < len(l):
    if l[i][0] == "s":   # check lowercase 's'
        print(f"Hello, {l[i]}")  # print the name, not the whole list
    i += 1  # move to next element

