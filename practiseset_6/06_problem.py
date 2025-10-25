"""write a program to calculate the grade of a student from his marks from the following scheme : 
90-100 -> Ex
80-90 -> A
70-80 -> B
60-70 -> C
50-60 -> D
<50 -> F  """

marks = int(input("enter your marks : "))
if marks<=100 and marks>=90 :
  print("congratulations you have Ex grade as your marks are", marks)
elif marks<90 and marks>=80 :
  print("congratulations you have A grade as your marks are", marks)
elif marks<80 and marks>=70 :
  print("congratulations you have B grade as your marks are", marks)
elif marks<70 and marks>=60 :
  print("congratulations you have C grade as your marks are", marks)
elif marks<60 and marks>=50 :
  print("congratulations you have D grade as your marks are", marks)
else :
  print("You have failed in exam .....better luck next time....!")