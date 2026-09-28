#1). Write a program to check whether the user entered number is 2 digit/ 3 digit/ 4 digit number
#2). Write a basic calculator program to perform Arithmetic operations
#3). Write a program to print the number of days in month
#4). Write a program to print the grades based on the following criteria:
#
#      91-100     Grade A
#      81-90      Grade B
#      71-80      Grade C
#      61-70      Grade D
#      Below 60   Grade E
# -----------------------------------------------------------------------------------------------

#1).
n=int(input("Enter a number:"))
if n>=10 and n<=99:
    print(n, " is a 2 digit number")
elif n>=100 and n<=999:
    print(n," is a 3 digit number")
else:
    print(n, " is a 4 digit number")

#2).
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
op=(input("Enter operator:"))
if op=='+':
    print("Sum is ",n1+n2)
elif op=='-':
    print("Difference is ",n1-n2)
elif op=='*':
    print("Difference is ",n1-n2)
elif op=='-':
    print("Product is ",n1*n2)
elif op=='/':
    print("Division is ",n1/n2)
elif op=='%':
    print("Modulus is ",n1%n2)
else:
    print("Floor is ",n1//n2)

#3).
month=input("Enter a month: ")
l1=['January','March','May','July','August','October','December']
l2=['April','June','September','November']
l3=['February']
if month in l1:
    print(month," contains 31 days")
elif month in l2:
    print(month," contains 30 days")
else:
    print(month," contains 28/29 days")

#4).
mark=int(input("Enter your mark: "))
if mark>=91 and mark<=100:
    print("Grade A")
elif mark>=81 and mark<=90:
    print("Grade B")
elif mark>=71 and mark<=80:
    print("Grade C")
elif mark>=61 and mark<=70:
    print("Grade D")
elif mark<60:
    print("Grade E")