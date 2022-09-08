# Average Height
# split and put it into a list
students_height = input("enter the height of the students and provide space between each heights \n ").split()
# range(from, to) - random no not including the end
# for loop
# typecasting strings into int
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
# adding all the heights of the students
heights = 0
for height in students_height:
    heights += height
# counting the number of students using for loop
no_of_students = 0
for no in students_height:
    no_of_students += 1
# calculating average height and printing it
average_height = heights / no_of_students
print(average_height)
