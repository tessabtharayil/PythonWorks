# for loop
# ========
# ____________________________________________.
# Syntax                                      |
# ------                                      |
# for iterating_variable in sequence:         |
#          statements to execute repeatedly   |
#                                             |
# sequence=string/list/tuple/set/dict/range() |
# ____________________________________________|

#1). Print the string "hello" using for loop
# ------------------------------------------
s="hello"
for i in s:
    print(i,end=" ")
print()

#2). Print a list of elements using for loop
# ------------------------------------------
l=['red','green','blue']
for i in l:
    print(i,end=" ")
print()

#3). Print a set of elements using for loop
# -----------------------------------------
s={1,2,3,4}
for i in s:
    print(i,end=" ")
print()

#4). Print dictionary sequence of elements using for loop
# -------------------------------------------------------
d={'a':10,'b':20,'c':30}
for i in d.items():
    print(i,end=" ")
print()

#5). Given list l=[12,34,56,45,89,16,69,33]
# Print each number in a list
# Print even numbers
# Print those numbers that are divisible by 5
# Print those numbers that contains digit 3
# --------------------------------------------
l=[12,34,56,45,89,16,69,33]
for i in l:
    print(i,end=" ")
print()
for i in l:
    if i%2==0:
        print(i,end=" ")
print()
for i in l:
    if i%5==0:
        print(i, end=" ")
print()
for i in l:
    if '3' in str(i):
        print(i, end=" ")
print()

#6). Given a string
# s="hello world"
# print each character
# print those characters that are not vowel
# -----------------------------------------
s ="hello world"
vowels="aeiouAEIOU"
for i in s:
    print(i,end=" ")
print()

print("Characters that are not vowels:")
for i in s:
    if i not in vowels:
        print(i,end=" ")
print()

#7). Given a dictionary
# d={'n1':23,'n2':46,'n3':89,'n4':24}
# print each value
# print odd values
# -----------------------------------
d = {'n1':23, 'n2':46, 'n3':89, 'n4':24}
for i in d.values():
    print(i,end=" ")
print()

print("Odd values:")
for i in d.values():
    if i%2!=0:
        print(i,end=" ")
print()

#8). Given a list l=["red",'green','orange','blue','black','yellow']
# print each color
# print color starting with 'b'
# print color whose length is greater than 5
# ------------------------------------------------------------------
l = ["red", "green", "orange", "blue", "black", "yellow"]
for i in l:
    print(i)
print()

print("Colors starting with 'b':")
for i in l:
    if 'b' in i[0]:
        print(i)
print()

print("Colors with length greater than 5:")
for i in l:
    if len(i) > 5:
        print(i)

#9).Given a list l=[10,'arun','amal',35,3.6,6.9,89]
# print  string values
# print float values
# -------------------------------------------------
l=[10,'arun','amal',35,3.6,6.9,89]
for i in l:
    if type(i)==str:
        print(i)
print()

for i in l:
    if type(i)==float:
        print(i)

#10). Given string l=[45,78,90,12,67]
# Print sum of digits
# Print product of even numbers
# print count of odd values
# -----------------------------------
l=[45,78,90,12,67]
sum=0
for i in l:
    sum+=i
print(sum)

product=1
for i in l:
    if i%2==0:
        product*=i
print(product)

count=0
for i in l:
    if i%2!=0:
        count+=1
print(count)
