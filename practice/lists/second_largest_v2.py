#Find Second Largest Number (Without using sort())
nums = [10, 5, 8, 20, 15]

largest = nums[0]
secondlargest = float('-inf')

for num in nums:
    if num > largest:
        secondlargest = largest
        largest = num
    elif num > secondlargest and num != largest:
        secondlargest = num

print(secondlargest)