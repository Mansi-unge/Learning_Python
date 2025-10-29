# write a python function to print multiplication table of a given number 

def table(n):
  i = 1 
  for i in range(i,11):
    num = n*i
    print(n,"X",i,"=",num)
  
n = int(input("enter any number of which you want table : "))
table(n)