#1). Given a string s="I am learning Python"
# find the length of the string
# find the reverse of the string
# find the last character of the strings
# find the 13th character
# print the characters from 2nd index to 15th index
# combine the string s with word "programming"

#2). Given a string s="python is a programming language"
# Remove the first 10 characters and print the remaining
# print the last 5 characters
#--------------------------------------------------------

#1).
s="I am learning Python"
print(len(s))
print(s[::-1])
print(s[-1])
print(s[12])
print(s[2:16])

#2).
print(s+" programming")
s="python is a programming language"
print(s[10:])
print(s[-5:])
