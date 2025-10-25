# write a program to create dictionary of hindi words with values as thier english translation provide user with an option to look it up !

words = {
  "help" : "madad" ,
  "fiver": "bukhar" ,
  "heaven" : "swarg" ,
  "friend" : "dost" ,
  "book" : "kitab"
}

word = input("write the word of which you want meaning in hindi : ")
print(words[word])