def op1_func1():
  print("your options are")
  for i in op1:
    print(i)

def op2_func2():
  print("your options are")
  for i in op2:
    print(i)

def op3_func3():
  print("your options are")
  for i in op3:
    print(i)

def op4_func4():
  print("your options are")
  for i in op4:
    print(i)

list1 = ["1.who developed python programming language.","2.which type of programming does python support.","3.Is python case sensitive when dealing with identifiers.","4.which of the following is used to define a block of code in python language."]

op1 = ["a) Wick van Rossum","b) Rasmus Lerdorf","c) Guido van Rossum","d) Niene Stom"]

op2 = ["a) object-oriented programming","b) structured programming","c) functional programming","d) all of the mentioned"]

op3 = ["a) no","b) yes","c) machine dependent","d) none of the mentioned"]

op4 = ["a) Indentation","b) Key","c) Brackets","d) All of the mentioned"]

list2 = []

a = 0
print("Press [1] to start or [0] to exit")

while a!=1:
  key = int(input("Press a key:-"))
  
  if key == 0:
    print("EXIT")
    break
    
  elif key == 1:
    for i in list1:
      print(f"{i}")
    
      if i == list1[0]:
        op1_func1()
      
        c =input("choose your option:-")
        if c == "c":
          print("you won",1000)
          list2.append(1000)
        else:
          print("you loose")
          break 
      
      elif i == list1[1]:
        op2_func2()
      
        c =input("choose your option:-")
        if c == "d":
          print("you won",2000)
          list2.append(2000)
        else:
          print("you loose")
          break 

      elif i == list1[2]:
        op3_func3()
      
        c =input("choose your option:-")
        if c == "b":
          print("you won",3000)
          list2.append(3000)
        else:
          print("you loose")
          break 
      
      elif i == list1[3]:
        op4_func4()
      
        c =input("choose your option:-")
        if c == "a":
          print("you won",4000)
          list2.append(4000)
        else:
          print("you loose")
          break
  
  else:
    print("Invalid key")
    continue
  a+=1 
  print(f"your total amount is:- {sum(list2)}")