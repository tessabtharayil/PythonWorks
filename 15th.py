# Nested conditionals
# ===================
#1). Write a program to check whether a number is even, odd or invalid number
# ----------------------------------------------------------------------------
num = input("Enter a number: ")
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Invalid number")

#2). Write a program to check the following:
#    a number is divisible by 2 and 3
#    a number is divisible by 2 and not divisible by 3
#    a number is divisible by 3 and not divisible by 2
#    a number is not divisible by 2 and 3
# ----------------------------------------------------
n=int(input("Enter a number: "))
if n%2==0:
    print(n," is divisible by 2")
    if n%3==0:
        print(n," is divisible by both 2 and 3")
    else:
        print(n," is not divisible by 3")
else:
    print(n," is not divisible by 2")
    if n%3==0:
        print(n, " is not divisible by 3")

#   OR
n=int(input("enter a number:"))
if n%2==0:
    if n%3==0:
        print("n is divisible by 2 and 3")
    else:
        print("n is divisible by 2 and not by 3")
elif n%3==0:
    print("n is divisible by 3 and not by 2")

else:
    print("n is not divisible by 2 amd 3")

#3). Write a program to check whether the entered number is positive-even or odd/negative-even or odd
# ---------------------------------------------------------------------------------------------------
n=int(input("Enter a number: "))
if n==0:
    print(n," is zero")
elif n>0:
    if n%2==0:
        print(n," is positive and even number")
    else:
        print(n," is positive and odd number")
else:
    if n % 2 == 0:
        print(n, " is positive and even number")
    else:
        print(n, " is positive and odd number")

