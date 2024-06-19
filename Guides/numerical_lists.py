# Generating a series of numbers using loop
for value in range(2, 10):
    print (value)
print()

# Creating a list of numbers with delimiter
numbers = list(range(1, 11, 2))
print (numbers)
print()

# Creating a list of even numbers
even_numbers = list(range(0, 12, 2))
print (even_numbers)

# Creating a list of square numbers
# Lets first craete an empty list for our square numbers to reside
squares = []
# Use a loop to get numbers from 1 - 10
for value in range(1, 11):
    # Created squares by squaring our values
    square = value ** 2
    # Append each square into the empty squares list
    squares.append(square)
# Coming out of the loop and prining just the list
print (squares)


# Lets aim to make the above code more concise 
# Create our empty squares list
square = []
# Create our for loop for our values
for value in range (1, 10):
    # Directly insering squares in by squaring the value in the append method 
    squares.append(value ** 2)
# Coming out of loop and printing the list
print (squares)

# Now lets use min, max and sum on our list
# Create a list called digits
digits = list(range(1, 100))
print (min(digits))
print (max(digits))
print (sum(digits))


# Creating a lis of values 
squares = []
for values in range(1, 11):
    squares.append(values ** 2)
print (squares)

# Create list of cars
cars = ["ford", "ferarri", "mustang", "jaguar"]
print (cars[0].title(), cars[1].title(), cars[2].title(), cars[3].title(), sep = ", ")

popped_car = cars.pop()
print (popped_car)

cars.append("jaguar")
print (cars)

del cars[1]
print (cars)

cars.insert(1, "jaguar")
print (cars)

cars.remove("ford")
print (cars)

cars.append("ford")
print (cars)

cars.sort()
print (cars)

cars.sort(reverse=True)
print (cars)

print (sorted(cars))
print (cars)

# do reverse, len and f string with a pop

cars.reverse()
print (cars)

print (len(cars))

# lets use an f string with a pop

popped_car = cars.pop(0)

message = (f"My favourite car was a 1990 {popped_car}.")
print (message)

print (f"My favourite car was a 1990 {popped_car}.")



# Lets make a list of cubed digits
cubes = []
for values in range(1, 11):
    cubes.append(values ** 3)
print (cubes)

# Lets print the numbers from 1 to 20
numbers = []
for digits in range(1,21):
    numbers.append(digits)
print (numbers)

# Making a list of numbers from 1 - a million
million_numbers = []
# for loop 
for digits in range(1, 1_000_000):
    numbers.append(digits)
print (numbers)
print (len(numbers))


# Lets bamke a list of cubed digits
cubes = []
for digits in range(1, 11):
    cubes.append(digits ** 3)
print (cubes)

# Lets try and make a list comprehension
cubes = [digits ** 2 for digits in range(1, 11)]
print (cubes)










