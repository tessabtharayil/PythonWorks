# #Create a package named Calculator containing single module operations.py
#
# in operations.py define
# add() --addition of two numbers
# sub()
# mul()
# div()

# write a program mymodule.py to import all these functions from the operations
# module and perform required operations using inputs:
from Calculator import operators

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operators.add(a,b)
operators.sub(a,b)
operators.mul(a,b)
operators.div(a,b)
print()

# #Create a package named Shapes containing modules circle.py  and
# rectangle.py

# define functions to calculate the area and perimeter of  circle and rectangle.

# write a program mymodule.py to import all these functions from the circle and
# rectangle modules and perform required operations.
from Shapes import circle,rectangle

r=int(input("Enter radius:"))
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
circle.area(r)
circle.perimeter(r)
rectangle.area(l,b)
rectangle.perimeter(l,b)