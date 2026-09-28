# List Comprehensive
# ==================
#1). Given a list i=[1,2,3,4]
# Create a new list with squares of each element
# ----------------------------------------------
l=[1,2,3,4]
new=[i**2 for i in l] #in each iteration adds i**2 where i takes value from list l
print(new)

new=[i**3 for i in l] #in each iteration adds i**3 where i takes value from list l
print(new)

new=[5 for i in l] #in each iteration adds 5 where i takes value from list l
print(new)

#2). Given a list l=[23,56,34,12,89,90,24]
# create a new list with even values
# create a new list with numbers greater than 50
# ----------------------------------------------
l=[23,56,34,12,89,90,24]
new=[i for i in l if i%2==0]
print(new)
new=[i for i in l if i>50]
print(new)

# Set Comprehension
# =================
#1). Given a string s="python coding is easy and fun"
# create a new list with only vowels
# ----------------------------------------------------
s="python coding is easy and fun"
new={i for i in s if i in "aeiouAEIOU"}
print(new)

# Dictionary Comprehension
# ========================
#1). Given a list l=[1,2,3,4]
# Create a new dictionary where keys are numbers and values are squares of each number
# ------------------------------------------------------------------------------------
l=[1,2,3,4]
new={i:i**2 for i in l}
print(new)

#2). Given a list l=[10,20,30,40]
# Create a new dictionary where keys are indexes and values are number
# --------------------------------------------------------------------
l=[10,20,30,40]
new={i:l[i] for i in range(0,len(l))}
print(new)

# Split
# =====
#________________________________.
# syntax-> sequence_name.split() |
# _______________________________|
s="hello world"
for i in s.split():
    print(i)

# 1). Given a string s="python coding is easy and fun"
# create a new dictionary where keys are words and values are length of each words
# --------------------------------------------------------------------------------
s="python coding is easy and fun"
new={i:len(i) for i in s.split()}
print(new)

