# negative slice 
# better to avoid negative slice
a = "ankita"#-6 -5 -4 -3 -2 -1
print(a[-6:7])
print(a[-7:-1]) 
print(a[-7:-1:-2])#❌
print(a[-7:-1:2])#Start index must be GREATER than end index


# a =  [start:end:step]
slicing = a [1:2:3]
print(slicing)