#Write a program to input eight numbers from the user and display all the unique numbers (once).
nums = {
    "num1": input("enter the number: "),
    "num2": input("enter the number: "),
    "num3": input("enter the number: "),
    "num4": input("enter the number: "),
    "num5": input("enter the number: "),
    "num6": input("enter the number: "),
    "num7": input("enter the number: "),
    "num8": input("enter the number: "),
}
unique = {}
for key in nums:
    if nums[key] not in unique:
        unique[nums[key]]= 1
        print(unique)