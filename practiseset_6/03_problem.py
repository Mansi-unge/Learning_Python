""" a spam comment is defined as a text containing following keywords :
"make a lot of money", "buy now","subscribe this","click this" - write a program to detect this spams
"""

comment = input("enter the comment : ")

if "make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment:
  print("this is spam message")
else:
  print("this is not spam message")