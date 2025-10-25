# write a program which finds out whether the given name is present in list or not 

name_list = []
name1 = input("enter your name : ")
name_list.append(name1)
name2 = input("enter your name : ")
name_list.append(name2)
name3 = input("enter your name : ")
name_list.append(name3)
name4 = input("enter your name : ")
name_list.append(name4)
name5 = input("enter your name : ")
name_list.append(name5)
name6 = input("enter your name : ")
name_list.append(name6)

print(name_list)

name = input("enter the name you want to search : ")

if name in name_list :
  print("your name is present in list")
else :
  print("your name is not present in list....try another name :")
  name = input("enter another name you want to search : ")
  if name in name_list :
    print("your name is present in list")
  else :
    print("your name is not present in list....better luck next time")