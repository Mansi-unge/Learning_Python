# write a python function which converts inches to centimeters 
#  fomula to convert inches to centimeters is ---->
#  centimeters = inches * 2.54


def inch_to_cm(inches) :
  cm = inches * 2.54
  return cm 

inches = int(input("enter inches value you want to convert it into centimeters : "))
print("the value of",inches,"in centemeters becomes",inch_to_cm(inches))