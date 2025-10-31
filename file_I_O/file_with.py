
# f = open("ex.txt")
# data = f.read()
# print(data)
# f.close()

# the same can be written using with statement like this : 

with open("file.txt") as f :
  print(f.read())

#you dont have to explicitely close the file