#                              Conditional Statements
#                              ======================

# if Statement
# ============
#1). Write a program using conditional statement to check if the age is 18 or older.
# Given that age=20
# ---
age=20
if age>=18:
    print("You are an adult.")

# if-else Flow
# ============
#2). Write a program to check whether the number is positive or negative
# ----------------------------------------------------------------------
n=int(input("Enter a number: "))
if n>=0:
    print(n," is a positive number")
else:
    print(n," is a neagative number")

#3). Write a program to check whether the number is even or odd
# -------------------------------------------------------------
n=int(input("Enter a number: "))
if n%2==0:
    print(n," is an even number")
else:
    print(n," is an odd number")

#4). Write a program to check whether the number is divisible by 3
# ----------------------------------------------------------------
n=int(input("Enter a number: "))
if n%3==0:
    print(n," is a divisible number of 3")
else:
    print(n," is not a divisible number of 3")

#5). Write a program to display a name if the entered name contains 'n' else print no
# -----------------------------------------------------------------------------------
n=input("Enter a name: ")
if 'n' in n:
    print("Name is ",n)
else:
    print("No")

#6). Write a program to display a name if the entered name starts with the letter 'n' else print no
# -------------------------------------------------------------------------------------------------
n=input("Enter a name: ")
if 'n' in n[0]:  # or n[0]=='n'
    print("Name is ", n)
else:
    print("No")

#7). Write a program to display a location if the entered location contains the word 'land' else print no
# -------------------------------------------------------------------------------------------------------
location = input("Enter a location: ")
if "land" in location:
    print("The location is ",location)
else:
    print("No")

#8). Write a program to find the greatest of two numbers
# ------------------------------------------------------
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1<n2:
    print(n2," is the greater than ",n1)
else:
    print(n1, " is the greater than ", n2)

#9). Write a program to check whether a person is eligible to vote or not
# ------------------------------------------------------------------------
name=input("Enter your name: ")
age=int(input("Enter your age: "))
if age>18:
    print(name," is eligible for voting")
else:
    print(name," is not eligible for voting")

# if-elif-else Chain
# ==================
#10). Write a program to check whether the number is divisible by 5 and ends with 5
# --------------------------------------------------------------------------------
n=int(input("Enter a number: "))
if n%10==5 and n%5==0:
    print(n," is divisible by 5 and ends with the number 5")
elif n%5==0:
    print(n, "is divisible by 5 but not ends with the number 5")
else:
    print(n,"is not divisible by 5 but not ends with the number 5")

#11). Write a program to check whether the number is positive, negative or zero
# ----------------------------------------------------------------------------
n=int(input("Enter a number: "))
if n>0:
     print(n," is a positive number")
elif n<0:
    print(n," is a negative number")
else:
    print(n," is a zero")

#12). Write a program to find the greatest of three numbers
# ---------------------------------------------------------
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
if n1>n2 and n1>n3:
    print(n1," is the greater than ",n2,"and",n3)
elif n2>n1 and n2>n3:
    print(n2, " is the greater than ",n1,"and",n3)
else:
    print(n3, " is the greater than ",n1,"and",n2)

