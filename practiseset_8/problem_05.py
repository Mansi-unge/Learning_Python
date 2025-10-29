"""write a python function to print first n lines of the following pattern 
***
**
* 

for n == 3
"""

def pattern(n) :
  if n == 0 :
    return 0
  print("*" * n)
  pattern(n-1)

n = int(input("enter any number n : "))
print("the pattern with the given number n =",n ,"is")
pattern(n)