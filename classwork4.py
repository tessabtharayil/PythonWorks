#1). Given a set s={10,20,30,40}
# Add a new number 50 to the set

#2). given a dictionary student_grade={'Alice':98,'Bob':85,'Charlie':74,'Mike':70}
# Print grade of Charlie
# Update the grade of Bob to 90
# Add new item 'Sam:75' to the dictionary
# Print the total number of students
# Print all student names in the given dictionary

#3). Given a dictionary student_marks={'Arun':{'maths':30,'science':35,'english':40,'history':33},
#                                      'Amal':{'maths':40,'science':45,'english':48,'history':43},
#                                      'Anu':{'maths':45,'science':46,'english':47,'history':49}}
# Print the mark of Amal in the subject History
# Update the mark of Arun in maths to 35
# Print the marks of all students (in all subjects)
# --------------------------------------------------------------------------------

#1).
s={10,20,30,40}
print(s)
s.add(50)
print(s)

#2).
student_grade={'Alice':98,'Bob':85,'Charlie':74,'Mike':70}
print(student_grade)
print(student_grade['Charlie'])
student_grade['Bob']=90
print(student_grade)
student_grade['Sam']=75
print(student_grade)
print(len(student_grade))
print(student_grade.keys())

#3).
student_marks={'Arun':{'maths':30,'science':35,'english':40,'history':33},
               'Amal':{'maths':40,'science':45,'english':48,'history':43},
               'Anu':{'maths':45,'science':46,'english':47,'history':49}}
print(student_marks)
print(student_marks['Amal']['history'])
student_marks['Arun']['maths']=35
print(student_marks)
print(student_marks.items())