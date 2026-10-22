
# Ternary Operator in Python
# Syntax: value_if_true if condition else value_if_false

# Example 1: Check eligibility by age
age = 15

result = "Eligible" if age >= 18 else "Not eligible"

print(result)  # Output: Not eligible


# Example 2: Check whether a number is positive or negative
number = int(input("Enter a number: "))

result = "Positive" if number > 0 else "Negative or zero"

print(result)
