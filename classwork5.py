#1). Write a program to check whether two entered numbers are equal or not
#2). Write a program to check whether two entered words are equal or not
#3). Write a program to find the maximum of two numbers
#4). Write a program to check whether the entered character is vowel or not
#5). Write a program to check whether the entered country name contains word 'land'
#6). Write a program to check whether the entered number is 3 digit or not
#7). Write a program to check whether the entered string is  palindrome or not
#8). Write a program to check whether a number is present in given list
#9). Write a program to check whether a key is prsent in a dictionary or not
#10). Write a program to check whether the given password is strong/weak(if length lessthan 8 weak)
# -------------------------------------------------------------------------------------------------

#1).
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1==n2:
    print(n1," and ",n2," are equal")
else:
    print(n1," and ",n2," are not equal")

#2).
s1=input("Enter first string: ")
s2=input("Enter second sting: ")
if s1==s2:
    print(s1," and ",s2," are equal")
else:
    print(s1," and ",s2," are not equal")

#3).
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1<n2:
    print(n2," is the greater than ",n1)
else:
    print(n1, " is the greater than ", n2)

#4).
ch=input("Enter the character: ")
vowel="aeiouAEIOU"
if ch in vowel:
    print(ch," is a vowel")
else:
    print(ch," is a consanant")

#5).
location = input("Enter a location: ")
if "land" in location:
    print("The country ",location," has land in its name")
else:
    print("The country ",location," does not have land in its name")

#6).
n=int(input("Enter a number:"))
if n>=100 and n<=999:
    print(n," is a 3 digit number")
else:
    print(n, " is not a 3 digit number")

#7).
s=input("Enter a string: ")
if s==s[::-1]:
    print(s," is paliandrome")
else:
    print(s," is not a palindrome")

#8).
n=int(input("Enter a number: "))
l=[23,67,12,90]
if n in l:
    print(n," is present in the list")
else:
    print(n," is not present in the list")

#9).
d={101:'Arun',102:'Amal',103:'Anu'}
key=int(input("Enter a number: "))
if key in d:
    print(key,"is present in the dictionary")
else:
    print(key, "is not present in the dictionary")

#10).
p=input("Enter the password: ")
if len(p)>8:
    print("Entered password is strong")
else:
    print("Entered password is weak")