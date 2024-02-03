fruit = ("Apples", 4, "bananas", 5, "Oranges" , 6 )
print(type(fruit))
List_0f_fruit = ["Apples", 4, "bananas", 5, "Oranges" , 6]
print(type(List_0f_fruit))
# lists can be modified# tuples lists cannot be modified
List_0f_fruit[0] = "strawberry"
print(List_0f_fruit)

print(fruit[1:5])

# concatenation of tuples
fruit = fruit[0:4] + ("cherries", 10)
print(fruit)

#tuples with one element
x = (5,)
print(type(x))

# the length of a tuple
print(len(fruit))






