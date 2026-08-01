nums = [0, 1, 0, 3, 12]

result = []

# Add non-zero numbers
for num in nums:
    if num != 0:
        result.append(num)

# Count zeros
zero_count = nums.count(0)

# Add zeros at end
for _ in range(zero_count):
    result.append(0)

print(result)