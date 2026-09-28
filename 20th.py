# Write a program to check whether a number is Armstrong number
# -------------------------------------------------------------
#Eg: 153-> 1^3+5^3+3^3 =153 then Armstrong
num=int(input("Enter a number: "))
sum=0
for i in str(num):
    sum=sum+int(i)**len(str(num))
if sum==num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


