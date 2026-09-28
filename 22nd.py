# Nested Loop
# ===========
#1). Given a list l=[10,20,30] print each element in the list 5 times
# -------------------------------------------------------------------
l=[10,20,30]
for i in l:
    for j in range(1,6):
        print(i,end=" ")
    print()

#20). Print the below elements in the given sequence order
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# ---------------------------------------------------------
for i in range(1,4):
    for j in range(1,5):
        print(i,end=" ")
    print()

#3). Print the below elements in the given sequence order
# * * * *
# * * * *
# * * * *
# --------------------------------------------------------
for i in range(1,4):
    for j in range(1,5):
        print('*',end=" ")
    print()

#4). Print the nested list using nested loop
# ------------------------------------------
l=[['lion','tiger'],['cat','elephant']] #Nested list
for i in l:
    print(i)
    for j in i:
        print(j)

#5). Given a list names=['kelly','alan','jeny']
# Print the list in the given sequence order
# kelly kelly kelly
# alan alan alan
# jeny jeny jeny
# ----------------------------------------------
names=['kelly','alan','jeny']
for i in names:
    for j in range(3):
        print(i, end=" ")
    print()

#6). Given 2 list names=[1,2,3] and q=['what','when','why']
# Print the list in the given sequence order
# 1
# what when why
# 2
# what when why
# 3
# what when why
# ----------------------------------------------------------
names =[1,2, 3]
q = ['what', 'when', 'why']
for i in names:
    print(i)
    for j in q:
        print(j,end=" ")
    print()

#7). Given a list d=[{'id':101,'name':'arun','age':23},
#                    {'id':102,'name':'amal','age':24},
#                    {'id': 103,'name':'anu','age':25}]
# Print each student details
# ID    NAME    AGE
# -----------------------------------------------------
d = [{'id':101,'name':'arun','age':23},
     {'id':102,'name':'amal','age':24},
     {'id': 103,'name':'anu','age':25}]
print("ID\t\t NAME\tAGE")
for i in d:
    print(i['id'],"\t",i['name'],"\t",i['age'])

#8). Print the below elements in the given sequence order
# *
# * *
# * * *
# * * * *
# -------------------------------------------------------
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=" ")
    print()

#9). Print the below elements in the given sequence order
# *
# * * *
# * * * * *
# * * * * * * *
# -------------------------------------------------------
for i in range(1,8,2):
    for j in range(i):
        print("*",end=" ")
    print()

#10). Print the below elements in the given sequence order
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# ---------------------------------------------------------
for i in range(1,5):
    for j in range(i):
        print(i,end=" ")
    print()

#11). Print the below elements in the given sequence order
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# --------------------------------------------------------
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#12). Print the below elements in the given sequence order
# * * * *
# * * *
# * *
# *
# --------------------------------------------------------
for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#13). Print all prime numbers from the given list
# l=[23, 45, 78, 90, 12, 13, 97]
# -----------------------------------------------
l = [23, 45, 78, 90, 12, 13, 97]
for i in l:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
print()

#14). Print all even numbers from the given list
# l=[23, 45, 78, 90, 12, 13, 97]
# ----------------------------------------------
for i in l:
    if i%2==0:
        print(i,end=" ")
print()

#15). Find all prime numbers in the range(1,100)
# ----------------------------------------------
for i in range(1,101):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
print()

#16). Find all Armstrong numbers in the range(100,1000)
# -----------------------------------------------------
for num in range(100,1000):
    sum=0
    for i in str(num):
        sum = sum+int(i)**len(str(num))
    if sum==num:
        print(num,end=" ")
print()

#17). Print the below elements in the given sequence order
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# ---------------------------------------------------------
for i in range(1,5):
    for j in range(1,6):
        print(j,end=" ")
    print()

#18). Print the below elements in the given sequence order
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# --------------------------------------------------------
k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print()

#19). Print the below elements in the given sequence order
# A
# B C
# D E F
# G H I J
# --------------------------------------------------------
k=ord('A')
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k+=1
    print()

#20). Print the below elements in the given sequence order
# A
# B B
# C C C
# D D D D
# --------------------------------------------------------
k=ord('A')
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(k),end=" ")
    k+=1
    print()

#21). Print the below elements in the given sequence order
# A
# A B
# A B C
# A B C D
# --------------------------------------------------------

for i in range(1,5):
    k=ord('A')
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k+=1
    print()

#22). Print the below elements in the given sequence order
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
# ---------------------------------------------------------
for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()

#23). Print the below elements in the given sequence order
# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
# ---------------------------------------------------------
for i in range(1,5):
    for j in range(1,5):
        if i==j:
            print(i,end=" ")
        else:
            print(0,end=" ")
    print()

#24). Print the below elements in the given sequence order
# 1
# 1 0
# 1 0 1
# 1 0 1 0
# ---------------------------------------------------------
for i in range(1,5):
    for j in range(1,i+1):
        if j%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()

#25). Print the below elements in the given sequence order
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# ---------------------------------------------------------
for i in range(1,5):
    for j in range(i+1):
        print(j,end=" ")
    print()

#26). Print the below elements in the given sequence order
# h
# h e
# h e l
# h e l l
# h e l l o
# ---------------------------------------------------------
s="hello"
for i in range(len(s)):
    for j in range(i+1):
        print(s[j], end=" ")
    print()

#27). Print the below elements in the given sequence order
#       *
#     * *
#   * * *
# * * * *
# -------------------------------------------------------
k=3*2
for i in range(1,5):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    k-=2
    print()

#28). Print the below elements in the given sequence order
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *
# --------------------------------------------------------
k=3*2
for i in range(1,5):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    k-=2
    print()
k=2
for i in range(3,0,-1):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    k+=2
    print()

#29). Print the below elements in the given sequence order
#       *
#     *   *
#   *   *   *
# *   *   *   *
#   *   *   *
#     *   *
#       *
# --------------------------------------------------------
k=3*2
for i in range(1,5):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end="   ")
    k-=2
    print()
k=2
for i in range(3,0,-1):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end="   ")
    k+=2
    print()

#30). Print the below elements in the given sequence order
#       1
#     1 2
#   1 2 3
# 1 2 3 4
#   1 2 3
#     1 2
#       1
# -------------------------------------------------------
k=3*2
for i in range(1,5):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="   ")
    k-=2
    print()
k=2
for i in range(3,0,-1):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="   ")
    k+=2
    print()

# 31). Print the below elements in the given sequence order
#       1
#     1   2
#   1   2   3
# 1   2   3   4
#   1   2   3
#     1   2
#       1
# -------------------------------------------------------
k=3*2
for i in range(1,5):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="   ")
    k-=2
    print()
k=2
for i in range(3,0,-1):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="   ")
    k+=2
    print()

