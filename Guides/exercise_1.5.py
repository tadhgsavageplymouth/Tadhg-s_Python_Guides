# Using a for loop to print the numbers from 1 to 20
list = []
for numbers in range(1, 21):
    list.append(numbers)
print (list)

# Making a list from one to a million and usnig for loop to print the numbers
list = []
for numbers in range(1, 1_000_001):
    list.append(numbers)
print (list)

# Printing the min number, max number and the sum of the list of numbers in the list
print (min(list))
print (max(list))
print (sum(list))

# Making a list of odd numbers from one to twenty
list = []
for numbers in range(1, 21, 2):
    list.append(numbers)
print (list)

# Making a list of the multiples of threee
multiples_three = []
for digits in range(3, 31, 3):
    multiples_three.append(digits)
print (multiples_three)

# Making a list of cubes from one to 10 
cubes = []
for digits in range(1, 11):
    cubes.append(digits ** 3)
print (cubes)

# Usage of list comprehensions to yeild the a list of cubes from one to 10
cubes = [digits ** 3 for digits in range(1, 11)]
print (cubes)

