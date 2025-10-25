# if languages of two friends are same than what will happen to the the program in problem 6 

dictionary = {}

friend1 = input("enter your name : ")
language1 = input("enter your favourite language : ")
dictionary.update({friend1:language1})

friend2 = input("enter your name : ")
language2 = input("enter your favourite language : ")
dictionary.update({friend2:language2})

friend3 = input("enter your name : ")
language3 = input("enter your favourite language : ")
dictionary.update({friend3:language3})

friend4 = input("enter your name : ")
language4 = input("enter your favourite language : ")
dictionary.update({friend4:language4})

print(dictionary)


"""
the output will be as follow :
enter your name : mansi
enter your favourite language : python
enter your name : rushi
enter your favourite language : java
enter your name : suraj
enter your favourite language : java
enter your name : chanchal
enter your favourite language : c
{'mansi': 'python', 'rushi': 'java', 'suraj': 'java', 'chanchal': 'c'}

because in dictionary keys must be unique values are allowed to be duplicated   """