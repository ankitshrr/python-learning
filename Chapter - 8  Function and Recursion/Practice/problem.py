# def greatestnumber(a,b,c):
#     if  a>b  and  a>c  :
#         print(f"{a} is the greatest number")
#     elif b>a and b>c:
#       print(f"{b} is the greatest number")
#     elif c >a and  c>b:
#      print(f"{c} is the greatest number")

# greatestnumber(20,12,23)
def greatestnumber(a,b,c):
    return max(a,b,c)
print(greatestnumber(2,3,4))