# Functions
# =========
#1). Define a function to find sum of two numbers
# -----------------------------------------------
def add():
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    s=n1+n2
    print("Sum is",s)
add()

#2). Define a function to display "hello your name"
# -------------------------------------------------
def hello():
    x=input("Enter your name:")
    print("hello,",x)
hello()

#3). Define a function to find the factorial of a number
# ------------------------------------------------------
def factorial():
    n=int(input("Enter a number:"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial()

#4). Define a function to find the count of a specific character in a given string
# --------------------------------------------------------------------------------
def count():
    s=input("Enter a string:")
    ch=input("Enter a character:")
    c= 0
    for i in s:
        if i == ch:
            c=c+1
    print(c)

count()

#5). Define a function to check whether a number is prime or not
# --------------------------------------------------------------
def prime():
    num = int(input("Enter a number:"))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not Prime Number")
                break
        else:
            print("Prime Number")
    else:
        print("Number is neither prime nor composite")
prime()

#6). Define a function to find the factors of a number
# ----------------------------------------------------
def fact():
    num=int(input("Enter a number:"))
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=" ")

fact()

# Function using parameters
# =========================
#1). Define a function using parameters to find sum of two numbers
# ----------------------------------------------------------------
def add(n1,n2):
    s=n1+n2
    print("Sum is",s)
add(23,24)

# OR
def add(a,b):
    s=n1+n2
    print("Sum is",s)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
add(a,b)

#2). Define a function that takes three arguments as amount, years and rate and find the simple interest value(dynamic input)
# ---------------------------------------------------------------------------------------------------------------------------
def simple_interest(p,n,r):
    si=(p*n*r)/100
    print("Simple Interest is ",si)
p = int(input("Enter amount:"))
n = int(input("Enter year:"))
r = int(input("Enter rate:"))
simple_interest(p,n,r)

# Return statement
# ================
#1). Define a function that takes two numbers as arguments and returns sum as result - call the function and print the result
# ---------------------------------------------------------------------------------------------------------------------------
def add(a,b):
    s=n1+n2
    return s
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
l=add(a,b)
print("Sum is",l)

#2). Define a function that takes a string as argument and return a new dictionary where keys are words and values are length of each word
# call the function and print the dictionary
# -----------------------------------------------------------------------------------------------------------------------------------------
def dic(s):
    new={}
    for i in s.split():
        new[i]=len(i)
    return new
s="python coding is easy and fun"
l=dic(s)
print(l)

# OR
def dic(s):
    new = {i: len(i) for i in s.split()}
    return new
s="python coding is easy and fun"
l=dic(s)
print(l)

#3). Define a function that takes a number as argument and check whether that number is spy number or not
# sum of digits=product of digits
# -------------------------------------------------------------------------------------------------------
def spy(s):
    sum=0
    product=1
    for i in s:
        sum+=int(i)
        product*=int(i)
    if sum==product:
            print("It is a spy number")
    else:
            print("It is not a spy number")
    return
s=input("Enter a number:")
spy(s)