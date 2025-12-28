import math

a = float(input("Enter base: "))
b = float(input("Enter height: "))

hypotenuse = round(math.sqrt(pow(a,2) + pow(b,2)),22)
print("Hypotenuse =", hypotenuse)
