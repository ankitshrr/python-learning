# Find Second Largest Number (Without using sort()) input [10, 5, 8, 20, 15]
nums = [10, 5, 8, 20, 15]
largest=nums[0]
second = nums[0]
for num in nums:
    if num >= largest:
        largest=num
    elif num > second and num != largest:
        second=num
print(largest)
print(second)
