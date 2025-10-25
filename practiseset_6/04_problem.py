# write a program to find out whether a given username contains less than 10 charachters or not 

username = input("enter your username :")
print("your username is : ",username)
characters = len(username)

if characters<=10 :
  print("there are less than 10 characters in you username")
else :
  print("there are greater than 10 characters in your username")