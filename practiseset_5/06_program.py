# create an empty dictionary. allow four friends to enter their favourite language as value and use the key as their names. Assumes that the names are unique

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