Operator = input('enter the operator')
num1 = float(input("enter the  first number"))
num2 = float(input("enter the  second number"))
if Operator == "+":
    result =round(num1 + num2)
    print(result)
elif Operator == "-":
    result =round( num1 - num2)
    print(result)
elif Operator == "*":
    result = round(num1 * num2)
    print(result)
elif Operator == "/":
    result = round(num1 / num2,2)
    print(result)
else:
    print("Error")
S
