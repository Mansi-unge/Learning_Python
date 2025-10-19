# write a program to fill in a letter template given below with the name and date 

letter = """
Dear <|name|>,
you are selected..!
<|date|> """

print(letter.replace("<|name|>","mansi").replace("<|date|>","28 oct 2025"))
