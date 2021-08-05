name = "Tyler"
greeting = "Hello " + name

# printing using a variable and an input function
print(greeting)

age = 24
print(age)

# Checking for the type of our variable
print(type(greeting))
print(type(age))

ageInWords = "2 years"

# this will create an error cant concatinate str with int
# print(name + " is  " + age + " years old")

parrot = "Norwegian Blue"
print(parrot)

# Prints the 3rd index of parrot which is w
print(parrot[3])
print()

# negative indexing
# prints the last number in the parrot variable which is e
print(parrot[-1])

# prints out the range of letters from indexs up to but not including first number to last number
print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we

# you dont need a first number but still new a :
print(parrot[:9])  # Norwegian

# if you leave out the last number it will go to the end of the string
print(parrot[10:])  # Blue

# if you dont put any numbers in it will print out the whole string
print(parrot[:])

# slicing using negative indexs
print(parrot[-4:-2])  # Bl
print(parrot[-4:12])  # Bl


print(parrot[0:6:2])  # Nre
print(parrot[0:6:2])  # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

# turns the string number into an array that contains the numbers in the string
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
