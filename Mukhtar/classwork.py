# Q1. Create a list of 5 students
# Q2. Using slicing, get the first two students
# Q3. Using slicing, get the last two students
# Q4. Create 2 variables holding a name each
# Q5. Using the right method, add the value of each of the variables to the list above
# Q6. Create an empty dictionary called student
# Q7. Using the right method, remove the first student from the list above and add it
# as a value in the above dictionary
# Q8. Remove the last two items from the above list and create a tuple with the values
# Q9. Add age, gender, hieght of the student into the student dictionary above using
# the most appropraite data types.
# Q10. Store a value for the student in the dictionary that indicates whether the student
# is admitted or not using a boolean.


# Q1. Create a list of 5 students
students = [ 'mukhtar',  'ali',  'kamal' ,  'rahman' ,  'suleiman' ]
# Q2. Using slicing, get the first two students
print(students[:2])
# Q3. Using slicing, get the last two students
print(students[3:5])
# Q4. Create 2 variables holding a name each
name = 'muhammad'
game = 'god of war'
print(name)
print(game)
# Q5. Using the right method, add the value of each of the variables to the list above.
students.extend(['muhammad' , 'god of war'])
print(students)
# Q6. Create an empty dictionary called student
student = {}
# Q7. Using the right method, remove the first student from the list above and add it
# as a value in the above dictionary
students.remove('mukhtar')
print(students)
x = student ={'name':'mukhtar'}
print(x)
# Q8. Remove the last two items from the above list and create a tuple with the values
students.remove('muhammad')
students.remove('god of war')
print(students)
people = 'muhammad' , 'god of war'
print(people)
# Add age, gender, hieght of the student into the student dictionary above using
# the most appropraite data types.
x.update({'age': 34 ,  })
x.update({'gender': 'm'})
x.update({'height':"6'3ft" })
print(x)
# Q10. Store a value for the student in the dictionary that indicates whether the student
# is admitted or not using a boolean.
student_info ={'name' : 'mukhtar', 'surname' : 'aliyy' , 'age' : 35}
admission_stat = True
print(student_info),
print(student_info.get('name'),
student_info.get('surname'),
'ad_stat;' , admission_stat)
