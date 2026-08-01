# find max & min without using max() and min().
nums = [5, 2, 9, 1, 7]
maxNums= nums[0]
MinNums= nums[0] 
for num in nums:
    if num >= maxNums:
        maxNums = num
    if num <= MinNums:
        MinNums = num
print(maxNums)
print(MinNums)

# find max & min  
print(max(nums))
print(min(nums))
