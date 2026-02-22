nums = [5, 2, 9, 1, 7]

max_num = nums[0]
min_num = nums[0]

for n in nums:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print("Max:", max_num)
print("Min:", min_num)