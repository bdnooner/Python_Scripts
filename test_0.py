name = input(("What is your name?: ")).upper()
print("Hello", name)
number_to_add = float(input("What numbers would you like to start with, " + name + "?: "))
additor = float(input("What is the value that you would like to add to the first number?: "))
total = number_to_add + additor
print(number_to_add, "+", additor, "=", total)
