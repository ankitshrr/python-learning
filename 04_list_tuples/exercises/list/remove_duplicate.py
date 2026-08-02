#Remove Duplicates BUT Keep order
nums = [6,1, 2, 2, 3, 4, 3, 5]
unique = []

for num in nums:
    if num not in unique:
      unique.append(num)
        
unique.sort()
print(unique)