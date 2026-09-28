#1). Define a function that takes 2 numbers and returns their product

#2). Define a function that takes a string and returns number of vowels

#3). Define a function that takes length and breadth and returns area of rectangle

#4). Define a function that takes a list of numbers and creates a new list with even numbers and returns the new list
# l=[45,78,90,12,35]

#5). Define a function that takes list of 3 digit numbers and returns a new list where each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]

#6). Define a function that takes a list and returns a new list containing unique elemnets from the given list
# l=[12,34,78,12,67,34,90,23]

#7). Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

#1).
def product(a,b):
    product=a*b
    return product
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
l=product(a,b)
print("Product =",l)

#2).
def vowels(s):
    count=0
    for i in s:
        if i in "aeiouAEIOU":
            count+=1
    return count
s=input("Enter a string:")
l=vowels(s)
print("Number of vowels =",l)

#3).
def area(length,breadth):
    a=length*breadth
    return a
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
s=area(l,b)
print("Area =",s)

#4).
def even(l):
    new=[]
    for i in l:
        if i%2==0:
            new.append(i)
    return new
l=[45,78,90,12,35]
s=even(l)
print(s)

#5).
def digit_sum(l):
    new=[]
    for i in l:
        sum=0
        for j in str(i):
            sum+=int(j)
        new.append(sum)
    return new
l=[123,345,111,678,134,809]
p=digit_sum(l)
print(p)

#6).
def unique(l):
    new=[]
    for i in l:
        if i not in new:
            new.append(i)
    return new
l=[12,34,78,12,67,34,90,23]
s=unique(l)
print(s)

#7).
def common(list1,list2):
    new=[]
    for i in list1:
        if i in list2:
            new.append(i)
    return new
list1 = [12, 34, 56, 78, 90]
list2 = [90, 34, 11, 57, 45]
s=common(list1,list2)
print(s)