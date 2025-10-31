"""write a program to generate multiplication tables from 2 to 20 and write it to the diffrent files. place these files in a folder for a 13-year old """

import os

def tables():
  os.makedirs("tables", exist_ok=True)
  max_tables = 20
  table_of = 2
  while table_of<=max_tables :
    print("lets create the table of ",table_of)
    
    table = open(f"tables/table{table_of}.txt" ,"w")
    i = 1
    while i<=10 :
      line = f"{table_of} X {i} = {table_of*i}\n"
      print(line.strip())
      table.write(line)
      i += 1
    table_of += 1
    table.close()

tables()


