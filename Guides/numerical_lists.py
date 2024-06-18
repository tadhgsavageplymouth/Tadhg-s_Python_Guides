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

# Lets create a list of the first 10 square numbers
# First create an empty list
squares = []
# For loop to create the numbers 1-10
for value in range(1, 11):
    # Now squaring our 1-10 values
    square = value ** 2
    # Appending squared values into list
    squares.append(square)
# Coming out of loop and printing our list
print (squares)





