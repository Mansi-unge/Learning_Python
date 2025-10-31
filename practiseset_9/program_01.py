# write a program to read the text from a given file 'poems.txt' and find out whetehr it contains the world 'twinkle'

f = open("poems.txt")
data = f.read()
print(data)

if "twinkle" in data :
  print("yes , word 'twinkle' is present in poems.txt ")
else:
  print("no, 'twinkle' word is not present in poems.txt")
f.close()