 #boolean loops and statements
#print(True)
#print(type(True))   # class bool
#print(type("True"))   # class str

# Testing  whether these statements are correct
# print(5 == 5)
# print(6 == 5)

# incorporating the if statement with a boolean
#x = 15
#y = 7

#if x % y == 0: # this means X divided by Y leaves a remainder of  0 then true if not false
  #  print(True)
#else:
  #  print(False)

# while loop
#number = 1
#while number < 4:
   # print(number)
    #if number == 2:
      #  break
    # number = number + 1

    # incorporating the else statement within the while loop
number = 1
while number < 4:
       print(number)
       number = number + 1
else:
      print("number is no longer less than 4")
number = -1
if number > 2:
       print("positive number")
elif number == 0:
         print("zero")
else:
        print("negative number")
