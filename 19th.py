#                                 Loop Control Statements
#                                 =======================
# break
# =====
s="hello"
for i in s:
    if i=='l':
        break
    print(i)
print("\n")

# continue
# ========
s="hello"
for i in s:
    if i=='l':
        continue
    print(i)

#1). Given a list of numbers l=[25,67,34,78,17,44,82]
# Print all number
# Stops the loop when i>50
# Skip all even numbers
# ---------------------------------------------------
l=[25,67,34,78,17,44,82]
for i in l:
    print(i,end=" ")
print()

for i in l:
    if i>50:
        break
    print(i)

for i in l:
    if i%2==0:
        continue
    print(i,end=" ")
print()

#2). Give a list colors = ['red', 'green', 'yellow', 'blue', 'orange', 'black']
# print all colors
# print those colors starting with 'b' #blue black
# print the first color starting with 'b' #blue
# skips all colors starting with 'b'
# -----------------------------------------------------------------------------
colors = ['red', 'green', 'yellow', 'blue', 'orange', 'black']
for i in colors:
    print(i,end=" ")
print()

for i in colors:
    if 'b' in i[0]:
        print(i,end=" ")
print()

for i in colors:
    if 'b' in i[0]:
        print(i,end=" ")
        break
print()

for i in colors:
    if 'b' in i[0]:
        continue
    print(i,end=" ")
print()

#3). Given s="python coding is easy and fun"
# print all charcters upto a specific character(including that character)
# -----------------------------------------------------------------------
s="python coding is easy and fun"

for i in s:
    print(i,end="")
print()

for i in s:
    print(i,end="")
    if 'y' in i:
        break
print()

# pass
# ====
# used for creating null block
for i in range(1,11):
    pass   # no operation
print(i)

for i in range(1,11):
    if i==3:
        pass
    else:
        print(i,end=" ")