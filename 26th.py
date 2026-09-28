# Built-in Functions
# ==================
# String
# ======
#1). Write a program to create a list of 5 random 3 digit numbers
# ---------------------------------------------------------------
import random
l=[]
for i in range(5):
    n=random.randint(100,999)
    l.append(n)
print(l)

#2). Write a program to create a 5 digit random otp number
# --------------------------------------------------------
import random
otp=random.randint(10000,99999)
print("OTP:",otp)

#3). Write a program to find the position of a character in a string
# ------------------------------------------------------------------
s=input("Enter a string: ")
ch=input("Enter a character: ")
print(s.index(ch))

#4). Define a function that takes a string as argument and returns a new dictionary where keys are character and values are count of each charcter
# ------------------------------------------------------------------------------------------------------------------------------------------------
def count_characters(s):
    d = {}

    for i in s:
        if i not in d:
            d[i]=s.count(i)
    return d
s=input("Enter a string: ")
print(count_characters(s))

#5). Define a function that takes string as argument and print the count of digits,spaces,letters in that string
# --------------------------------------------------------------------------------------------------------------
def count(s):
    digit=0
    space=0
    letter=0
    for i in s:
        if i.isdigit():
            digit=digit+1
        elif i.isspace():
            space=space+1
        elif i.isalpha():
            letter=letter+1
    print("Digits:", digit)
    print("Spaces:", space)
    print("Letters:", letter)
s=input("Enter a string: ")
count(s)

