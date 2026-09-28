#1). Declare a list of 5 colours
#2). Add a new colour 'yellow' to the list
#3). Change the second colour to black
#4). Print the list in reverse order
#5). Print the second last colour
#6). Print the number of colours
#7). Print the updated list
# -----------------------------------------

#1).
l=['red','white','rose','orange','blue']
print(l)

#2).
l.append('yellow')
print(l)

#3).
l[1]='black'
print(l)

#4).
print(l[::-1])

#5).
print(l[-2])

#6).
print(len(l))

#7).
print("Updated list:",l)