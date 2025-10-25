# write a number to find the greatest of four numbers entered by the user 

num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))
num3 = int(input("enter the third number : "))
num4 = int(input("enter the fourth number : "))

print("numbers you entred are : " , num1 ,num2,num3,num4)
if num1>num2 and num1>num3 and num1>num4 :
  print("num1 is greater than all other numbers....")
elif num2>num3 and num2>num4 and num2>num1 :
  print("num2 is greater than all other numbers....")
elif num3>num2 and num3>num4 and num3>num1 :
  print("num3 is greater than all other numbers....")
else :
  print("num4 is greater than all other numbers....")