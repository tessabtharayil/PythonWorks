# List
# ====
l=[1,2,3]
l.append(5)
print(l)
l.extend((6,7,8))
print(l)

l=[89,45,4,27,99,25]
l.sort()
print(l)
l.pop()
print(l)
l.pop(2)
print(l)

l=[10,20,30,40,50,60]
l.insert(2,70)
print(l)
l.remove(30)
print(l)

#1). Given a list l=[1,2,2,3,4,4,5,6]
# create a new dictionary where keys are numbers and values are number occurence of each number
# ---------------------------------------------------------------------------------------------
l=[1,2,2,3,4,4,5,6]
new={}
for i in l:
    new[i]=l.count(i)
print(new)

#2). Given a list l=[11,34,78,23,90,65]
# find the largest number
# find the second largest number
# find the smallest number
# find the second smallest number
# --------------------------------------
l=[11,34,78,23,90,65]
print("Largest number is",max(l))
l.sort()
print("Second largest number is",l[-2])
print("Smallest number is",min(l))
print("Second smallest number is",l[1])

#3). Given a list l=[['arun',23,30000],['amal',25,50000],['anu',27,40000]]
# find the maximum salary
# find the mininum age
# ------------------------------------------------------------------------
l=[['arun',23,30000],['amal',25,50000],['anu',27,40000]]
print("Maximum salary is",max(i[2] for i in l))
print("Minimum age is",min(i[1] for i in l))

#4). Given a list l=[23,45,67,12,90,78]
# find the largest number,smallest number without using built in method
# ---------------------------------------------------------------------
l=[23,45,67,12,90,78]
max=l[0]
for i in l:
    if i>max:
        max=i
print("Largest number is",max)

min=l[0]
for i in l:
    if i<min:
        min=i
print("Smallest number is",min)

