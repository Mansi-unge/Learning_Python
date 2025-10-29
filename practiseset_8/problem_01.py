# write a program using functions to find greatest of all three numbers 

a = int(input("enter your number : "))
b = int(input("enter your number : "))
c = int(input("enter your number : "))

def greatest(a,b,c) :
  if(a>b and a>c):
    print("a is the greatest number...!")
  elif(b>a and b>c):
    print("b is the greatest number...!")
  else:
    print("c is the greatest number...!")


greatest(a,b,c)