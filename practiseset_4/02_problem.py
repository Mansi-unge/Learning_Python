# write a program to accept marks of six students and display them in a sorted manner 

student_marks = []

student1_marks = int(input("marks of student 1 is : "))
student_marks.append(student1_marks)
student2_marks = int(input("marks of student 2 is : "))
student_marks.append(student2_marks)
student3_marks = int(input("marks of student 3 is : "))
student_marks.append(student3_marks)
student4_marks = int(input("marks of student 4 is : "))
student_marks.append(student4_marks)
student5_marks = int(input("marks of student 5 is : "))
student_marks.append(student5_marks)
student6_marks = int(input("marks of student 6 is : "))
student_marks.append(student6_marks)
print(student_marks)
student_marks.sort()
print(student_marks)