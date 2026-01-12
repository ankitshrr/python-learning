n = int(input("enter the  the number to check prime or not :"))
is_prime = True
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("it is not prime", n)

        else:

            print("it is  prime")
