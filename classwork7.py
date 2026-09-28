#1). Write a program to find BMI(Body Mass Index)
# BMI= weight in (kg)/ height**2 in (m)
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese
#     from platform import processor

#2). A toy vendor supplies three types of toys:
#
# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.
# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

#3). FIZZBUZZ Problem
#
# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
# otherwise else -print the number
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#1).
w=int(input("Enter your weight(kg): "))
h=float(input("Enter your height(m): "))
bmi=w/(h**2)
print("Body Mass Index: ",bmi)
if bmi<=18.4:
    print("Status: Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Status: Normal")
elif bmi>=25.0 and bmi<=39.9:
    print("Status: Overweight")
elif bmi>=40.0:
    print("Status: Obese")

#2).
#code 1-battery based
#code 2-key based
#code 3-electrical based
code=int(input("Enter the code:"))
price=float(input("Enter the price:"))
if code==1:
    if price>=1000:
        d=price-(price*0.10)
        print("Price: ",d)
    else:
        print("No Discount for this product")
elif code==2:
    if price>=100:
        d=price-(price*0.05)
        print("Price: ",d)
    else:
        print("No Discount for this product")
elif code==3:
    if price>=500:
        d=price-(price*0.10)
        print("Price: ",d)
    else:
        print("No Discount for this product")
else:
    print("Invalid product code")

#3).
n=int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print(n)