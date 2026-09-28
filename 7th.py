# Swapping Numbers
# ================
#1). Write a program to interchange(swap) two variables using 3 variables
# -----------------------------------------------------------------------
a=2
b=3
temp=b
b=a
a=temp
print(a)
print(b)

#2). Write a program to interchange(swap) two variables without using third variable (1st method)
# -----------------------------------------------------------------------------------------------
a=2
b=3
a,b=b,a
print(a)
print(b)

#3). Write a program to interchange(swap) two variables without using third variable (2nd method)
# -----------------------------------------------------------------------------------------------
a=2
b=3
a=a+b
a=a-b
b=a-b
print(a)
print(b)