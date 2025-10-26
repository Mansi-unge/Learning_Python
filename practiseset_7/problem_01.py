# write a program to print multiplication table of a given number using for loop 

table = int(input("enter which table you want to print :"))

for i in range(1,11) :
  print(table , "X" , i , "=", table*i)