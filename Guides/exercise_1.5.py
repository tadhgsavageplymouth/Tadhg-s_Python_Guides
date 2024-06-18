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

