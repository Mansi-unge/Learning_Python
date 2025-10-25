# if the names of two friend are same ; what will happen to the program in problem 6 


dictionary = {}

# 1st friend
friend1 = "mansi"
language1 = "python"
dictionary.update({friend1: language1})
# dictionary = {'mansi': 'python'}

# 2nd friend
friend2 = "rushi"
language2 = "java"
dictionary.update({friend2: language2})
# dictionary = {'mansi': 'python', 'rushi': 'java'}

# 3rd friend
friend3 = "rushi"  # SAME name again!
language3 = "node"
dictionary.update({friend3: language3})
# 'rushi' already exists, so it overwrites the old value
# dictionary = {'mansi': 'python', 'rushi': 'node'}

# 4th friend
friend4 = "chanchal"
language4 = "c"
dictionary.update({friend4: language4})
# dictionary = {'mansi': 'python', 'rushi': 'node', 'chanchal': 'c'}
