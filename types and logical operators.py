# python types

print(type("Hello, World"))
print(type(13))
print(type(4.72))
print(type(True))

print(4.72, int(4.72))# python rounds down
print(4.05, int(4.05))
# rounding up
print(4.72, int(4.72), int(round(4.72)))

# moving strings to integers cannot have letters
print("12345", int("12345"))

# moving to floats

print(float(18))

# moving to strings
print(str(18))
print(str(19.5))
print(type(str(19.5)))

# logical operators and,or,not
x = 6
print(x > 0 and x < 5)
y = 24
print(y % 2 == 0 or y% 5 == 0)







