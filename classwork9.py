#1). Create a new list of cubes l=[1,2,3,4]

#2). Create a new list of square roots l=[25,36,81,100]

#3). Create a new list of lengths colors=['red','green','blue','yellow','black']
# create a new list of first characters
# create a new list of last characters
# create a new list of reverse of each element

#4). Given a list l=[23,78,12,56]
#Add 10 to each element in the given sequence

#5). given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# create a new list of emails

#6).create a new list with square root of each element from the list l=[25,16,9,36]

#7). Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# create a list of names
# create a list of marks

#8). Given a list l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
# create a list of string values
# create a list of floats
# create a list of positive numbers

#9). Given a list fruits=['apple','orange','pineapple','avocado','grapes']
# create a new list with elements whose length is greater than 6

#10). create a new list with elements whose value is divisible by 3 in range(1,101)

#11). Given s="python coding  is easy and fun"
# create a new list with only vowels
# ---------------------------------------------------------------------------------

#1).
l=[1,2,3,4]
new=[i**3 for i in l]
print(new)

#2).
l=[25,36,81,100]
new=[i**0.5 for i in l]
print(new)

#3).
colors=['red','green','blue','yellow','black']
new=[len(i) for i in colors]
print(new)

new=[i[0] for i in colors]
print(new)

new=[i[-1] for i in colors]
print(new)

new=[i[::-1] for i in colors]
print(new)

#4).
l=[23,78,12,56]
new=[i+10 for i in l]
print(new)

#5).
l = [{'empid': 100, 'name': 'arun', 'salary': 20000, 'email': 'arun@gmail.com'},
     {'empid': 101, 'name': 'amal', 'salary': 25000, 'email': 'amal@gmail.com'},
     {'empid': 102, 'name': 'anu', 'salary': 30000, 'email': 'anu@gmail.com'}]
emails=[i['email'] for i in l]
print(emails)

#6).
l=[25,16,9,36]
new=[i**0.5 for i in l]
print(new)

#7).
d={'arun':25,'amal':34,'akhil':26,'anu':21}
new=[i for i in d.keys()]
print(new)

new=[i for i in d.values()]
print(new)

#8).
l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
new=[i for i in l if type(i)==str]
print(new)

new=[i for i in l if type(i)==float]
print(new)

new=[i for i in l if type(i)!=str and i>0]
print(new)

#9).
fruits=['apple','orange','pineapple','avocado','grapes']
new=[i for i in fruits if len(i)>6]
print(new)

#10).
new=[i for i in range(1,101) if i%3==0]
print(new)

#11).
s="python coding  is easy and fun"
new=[i for i in s if i in 'aeiouAEIOU']
print(new)