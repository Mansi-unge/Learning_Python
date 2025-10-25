# write a program to find out whether a student has passed or failed if it is requires a total of 40%  and atleast 30% in each subject to pass. Assume 3 subjects and take marks as an input from the user 

Maths = int(input("enter your marks obtained in maths :"))
science = int(input("enter your marks obtained in science :"))
English = int(input("enter your marks obtained in English :"))

print("marks of a student in maths is ",Maths,",in science it is ",science,"and in english it is ",English)
percentage = (Maths + English + science)/3
print("percentage scored by student is :", percentage)

if Maths<30 or science<30 or English<30 :
  print("you have failed in one or more subject")
elif percentage >= 40 :
  print("you have passed in exam")
else:
  print("you have failed in exam...better luck next time")
  