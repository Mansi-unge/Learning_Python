# write a python program using functions to convert celsius to fahrenheit
# formula --->  f = (c*9/5)+32

def celcius_to_farhrenheit(C) :
  F = (C*9/5)+32
  return F


C = float(input("enter the temperature in celcius :"))
print("value of given celcius to fahrenheit is : ", celcius_to_farhrenheit(C))