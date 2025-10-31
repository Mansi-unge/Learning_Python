# the game() function is a program lets the user play a game and return the score  as an integer . you need to read a file 'hi-score.txt' which is either blank or contains the previous hi-score. you need to write a program to update the hi-score whenevr the game() function breaks the hi-score.

import random


def check_score(user_input , computer_input):
  if user_input == computer_input :
    print("it's a draw..!")
    return 0 
  elif user_input > computer_input :
    print("you won..!")
    return 10 
  else :
    print("you lost..!")
    return 0
  


def game() :
  print("welcome to the game :")
  print("-"*100)
  user_input = int(input("enter any random number you want between 1 to 100 :"))
  print("user input :",user_input)

  computer_input = random.randint(1,100)
  print("computer input :",computer_input)

  score = check_score(user_input , computer_input)

  try :
    with open("hi-score.txt") as f:
      content = f.read()
      if content.strip() =="":
        hi_score = 0
      else:
        hi_score = int(content)
  except FileNotFoundError:
    hi_score = 0

  print(f"your score : {score} , previous hi-score : {hi_score} ")

  if score > hi_score :
    with open("hi-score.txt","w") as f:
      f.write(str(score))
    print("new Hi-Score Acheived...!")
  elif computer_input > user_input:
    print("Try again to beat the hi-score")

game()