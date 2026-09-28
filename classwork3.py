#1). Given a string s="Python coding is easy and fun"
# find the length of the string
# find the reverse of the string
# find the last character of the string

#2). Given a list l=['Guitar','Piano','Violin','Drums','Flute']
# Add a new item 'Veena' to the list

#3). Declare a list of 5 food items
# Add new food item to the list
# change the second food item
# print the updated list
# print the last food item
# print the number of food items

#4). Given a string s1="python is a programming language"
# Remove the first 10 characters and print the remaining
# print the last 5 characters
# ------------------------------------------------------

#1).
s="Python coding is easy and fun"
print(s)
print(len(s))
print(s[::-1])
print(s[-1])

#2).
l=['Guitar','Piano','Violin','Drums','Flute']
print(l)
l.append('Veena')
print(l)

#3).
t=['laddo','samoosa','puffs','burger','pizza']
print(t)
t.append('chappathi')
print(t)
t[1]='biriyani'
print(t)
print("Updated list:",t)
print(t[-1])
print(len(t))

#4).
s1="python is a programming language"
print(s1)
print(s1[10:])
print(s1[-5:])
