# while loop
# ==========
# _____________________________.
# Syntax:                      |
# -------                      |
# i=1 #initialization          |
# while(i<=10):                |
#     print(i) #statement      |
#     i=i+     #incrementation |
# _____________________________|

#1). 1, 4, 9, 16, 25
# ------------------
i=1
while i<=5:
    print(i*i,end=" ")
    i+=1 #i=i+1
print("\n")

#2). 1,2,3,4,5,.....100
# ---------------------
i=1
while i<=100:
    print(i,end=" ")
    i+=1
print("\n")

#3). 1,3,5,7,9,11,13,15
# ---------------------
i=1
while i<=15:
    print(i,end=" ")
    i+=2
print("\n")

#4). 2,4,6,8,10,12
# ----------------
i = 2
while i <= 12:
    print(i, end=" ")
    i += 2
print("\n")

#5). 1,4,7,10,13,16
# -----------------
i=1
while i<=16:
    print(i,end=" ")
    i+=3
print("\n")

#6). 10,20,30,40,50,60,70,80
# --------------------------
i=10
while i<=80:
    print(i,end=" ")
    i+=10
print("\n")

#7). 3,6,9,12,15,18,21
# --------------------
i=3
while i<=21:
    print(i,end=" ")
    i+=3
print("\n")

#8). 5,4,3,2,1
# ------------
i=5
while i>=1:
    print(i,end=" ")
    i-=1
print("\n")

#9). 8,6,4,2,0
# ------------
i = 8
while i>=0:
    print(i, end=" ")
    i-=2
print("\n")

#10). 100,101,102,.....200
# ------------------------
i=100
while i<=200:
    print(i,end=" ")
    i+=1
print("\n")

#11). Print all 4 digit numbers(1000-9999)
# ----------------------------------------
i=1000
while i<=9999:
    print(i,end=" ")
    i+=1

#12). Print those numbers that are divisible by 3 in the range(1,50)
# ------------------------------------------------------------------
i=1
while i<=50:
    if i%3==0:
        print(i,end=" ")
    i+=1

#13). Count those numbers that are divisible by 3 in the range(1,50)
# ------------------------------------------------------------------
i=1
count=0
while i<=50:
    if i%3==0:
        print(i,end=" ")
        count+=1
    i+=1
print("\nCount=",count)

#14). Print those 3 digits number that are divisible by 5 and 7
# -------------------------------------------------------------
i=100
while i<=999:
    if i%5==0 and i%7==0:
        print(i,end=" ")
    i+=1

#15). Print those numbers in the range(100, 200) which contains digit '3'
# -----------------------------------------------------------------------
i=100
count=0
while i<=200:
    if '3' in str(i):
        print(i,end=" ")
        count+=1
    i+=1
print("\nCount=",count)

#16). Find the sum of series 1,2,3,4,5
# ------------------------------------
i=1
sum=0
while i<=5:
    sum+=i
    i+=1
print("Sum is ",sum)

#17). Find the product of series 1,2,3,4,5
# ----------------------------------------
i=1
pro=1
while i<=5:
    pro*=i
    i+=1
print("Product is ",pro)

#18). Find the sum of first 10 even number
# ----------------------------------------
i=1
sum=0
while i<=20:
    sum+=i
    i+=2
print("Sum is ",sum)

#19). Find the product of first 10 even numbers
# ---------------------------------------------
i=1
pro=1
while i<=20:
    pro*=i
    i+=2
print("Product is ",pro)

#20). Print series 4,9,14,19,24,29,34,39
# --------------------------------------
i=4
while i<=39:
    print(i,end=" ")
    i+=5

#21). Print sum of series 1,3,5,7,9,11
# ------------------------------------
i=1
sum=0
while i<=11:
    sum+=i
    i+=2
print("\nSum is ",sum)

#22). Print product of numbers that are divisible by 3 and 5 in the range(1,50)
# -----------------------------------------------------------------------------
i=1
pro=1
while i<=50:
    if i%3==0 and i%5==0:
        pro*=i
    i+=1
print("Product is ",pro)

#23). Count of 3 digit numbers that are divisible by 7
# ----------------------------------------------------
i=100
count=0
while i<=999:
    if i%7==0:
        count+=1
    i+=1
print("Count is ",count)

#24). Factorial of a number
# -------------------------
i=1
n=int(input("Enter a number: "))
fact=1
while i<=n:
    fact*=i
    i+=1
print("Factorial is ",fact)

#25). Multiplication table of a number
# ------------------------------------
n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n,'*',i,'=',n*i)
    i+=1
