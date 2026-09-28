# Map
# ===
# Example
# -------
l=[1,2,3,4]
print(list(map(lambda x:x**2,l)))
print(tuple(map(lambda x:x**2,l)))
print(set(map(lambda x:x**2,l)))

#1). Create a new list of cubes using the given list l=[1,2,3,4]
# --------------------------------------------------------------
l=[1,2,3,4]
print(list(map(lambda x: x**3, l)))

#2). Create a new list of square roots using the given list l=[25,36,81,100]
# --------------------------------------------------------------------------
l=[25,36,81,100]
print(list(map(lambda x: x**0.5, l)))

#3). Create a new list of lengths using the given list colors=['red','green','blue','yellow','black']
#create a new list of first characters
#create a new list of last characters
#create a new list of reverse of each element
# ----------------------------------------------------------------------------------------------------
colors=['red','green','blue','yellow','black']
print(list(map(lambda x: len(x), colors)))

print(list(map(lambda x: x[0], colors)))

print(list(map(lambda x: x[-1], colors)))

print(list(map(lambda x: x[::-1], colors)))

#4). Given a list l=[23,78,12,56]
# Add 10 to each element in the given sequence
# --------------------------------------------
l = [23, 78, 12, 56]

print(list(map(lambda x: x + 10, l)))

#5). Given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# create a new list of emails
# -----------------------------------------------------------------------
l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
   {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
   {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
print(list(map(lambda x: x['email'], l)))
