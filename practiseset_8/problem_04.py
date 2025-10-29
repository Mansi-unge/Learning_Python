# write a recursive function to calculate the sum of the first n natural numbers 

def sum(n):
    if n == 1:
        return 1 
    else :
        return n + sum(n-1)
    

n = int(input("enter the number n of which you want the sum : "))
print("the sum of n natural number", n ,"is",sum(n))