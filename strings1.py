# Strings
print("Hello, World")
print(type("Hello, World"))
# Operations on strings
# addition sign concatenation
Greeting = " hello"
name = " Tony"
print(Greeting + name)
# * operator
print(Greeting*3)
print(Greeting + name*3)
print((Greeting + name)*3)

#Index operator
name = "brad"
#print(name[1]) # b = 0
#print(name[0] + name[3])
# slicing strings
print(name[0:4])
print(name[:2])
print(name[2:])

# lowercase and uppercase
name ="roger"
print(name.lower())
print(name.upper())
#count how many times a character appears in a string
print(name.count("r"))
#replace specific character  with other character
print(name.replace("r", "d"))
name = "tony"
New_name = name.replace("t", "j")
print(New_name)
# finding the length of a string
print(len(name))
# format strings
#your_name = input(" your name:")
#hello = " Hello {}".format(your_name)
#print(hello)

print("orange" < "strawberry")
print(ord('o')) # python assigns a value
print(chr(38))

# in and not operators
fruit = "banana"
print("a" in fruit)
print("s" not in fruit)
x = "hello"
y = ""
for character in x:
    y = character.upper() + y
    print(y)

    



