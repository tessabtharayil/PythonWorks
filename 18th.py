# Range
# =====
#1). Print series 1,2,3,4,5
# -------------------------
for i in range(1,6):
    print(i,end=" ")
print()

#2). Print series 1,3,5,7,9
# -------------------------
for i in range(1,10,2):
    print(i,end=" ")
print()

#3). Print series 2,4,6,8,10
# --------------------------
for i in range(2,11,2):
    print(i,end=" ")
print()

#4). Print series 1,4,9,16,25
# ---------------------------
for i in range(1,6):
    print(i*i,end=" ")
print()

#5). Print series 4,9,14,19,24,29,34,39
# -------------------------------------
for i in range(4,40,5):
    print(i,end=" ")
print()

#6). Print series 5,4,3,2,1
# -------------------------
for i in range(5,0,-1):
    print(i,end=" ")
print()

#7). Print series 8,6,4,2,0
# -------------------------
for i in range(8,-1,-2):
    print(i,end=" ")
print()

#8). Print series 7,14,21,28,35,42
# --------------------------------
for i in range(7,43,7):
    print(i,end=" ")
print()

#9). Print series 100,200,300,.....1000
# --------------------------------------
for i in range(100,1001):
    print(i,end=" ")
print()

#10). Print series 1,8,27,64,125
# ------------------------------
for i in range(1,6):
    print(i*i*i,end=" ")
print()

#11). Find all 3 digit numbers that are divisible by 3
# ----------------------------------------------------
for i in range(100,1000):
    if i%3==0:
        print(i,end=" ")
print()

#12). Print the list colors=['red','green','blue','yellow','black']
# -----------------------------------------------------------------
colors=['red','green','blue','yellow','black']
for i in colors:
    print(i,end=" ")
print()

#13). Print reverse of each color
# -------------------------------
for i in colors:
    print(i[::-1],end=" ")
print()

#14). Print each digit in a number
# --------------------------------
# n=int(input("Enter a number: "))
# for i in str(n):
#     print(i,end=" ")
#print()

#15). Print sum of digits in a number
# -----------------------------------
# n=int(input("Enter a number: "))
# sum=0
# for i in str(n):
#     sum=sum+int(i)
#     print(sum)

#16). Given list l=[1,2,3,4]
# create a new list with sequence of each number [1,4,9,16]
# ---------------------------------------------------------
l=[1,2,3,4]
new=[]
for i in l:
    new.append(i**2)
print(new)

#17). Given set s={1,2,3,4}
# create a new set with sequence of each number {1,4,9,16}
# --------------------------------------------------------
s={1,2,3,4}
new=set()
for i in s:
    new.add(i**2)
print(new)

#18). Given string s="hello world"
# create a new string with only vowels (new="eoo")
# ------------------------------------------------
s="hello world"
new=""
vowels="aeiouAEIOU"
for i in s:
    if i in vowels:
        new+=i
print(new)

#19). Create a new dictionary where keys are numbers and values are the square of each number
# -------------------------------------------------------------------------------------------
l=[1,2,3,4]
new={}
for i in l:
    new[i]=i**2
print(new)

#20). Print reverse of a string
# -----------------------------
s="hello"
rev=""
for i in s:
    rev=i+rev  #or [::-1]-but somecases not possible
print(rev)

#21. Reverse of a number
# -----------------------
n=1234
rev=""
for i in str(n):
    rev=i+rev
print(rev)

#22). Factors of a number
# -----------------------
num=int(input("Enter a number:"))
for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")