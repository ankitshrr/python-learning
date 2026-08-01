#Remove duplicates
nums = [5, 2,2, 9, 1, 7]
unique =[]
for num in nums :
    if num  not in unique:#membership operator "not in" if element doesnt exist 
        unique.append(num)
print(unique)
