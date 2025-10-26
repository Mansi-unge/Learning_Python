# write a program to find whether a given number is prime or not 

no = int(input("enter any number :"))

for i in range(2,no):
  if(no%i) == 0 :
    print("number is not prime")
  break

