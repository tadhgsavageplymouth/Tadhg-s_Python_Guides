### Making of a simple list
cars = ["jaguar", "range rover", "jaguar"]

### Printing of the entire list yeilds the entire list with symbols 
print (cars)

### Calling an individual item in the list
print (cars[0])

### Calling an individual item in the list with title for formatting 
print (cars[1].title())

### Calling an individual item in the list placing all in capital letters
print (cars[1].upper())

### Accessing the last item in a list use -1 to access it 
print (cars[-1].title())

### Accessing the second and third last item in a list using -2 and -3, this can be continued
print (cars[-2].title())
print (cars[-3].title())

### Using f string to make a message from our list
message = f"My first car was a {cars[0].title()}, I really liked the car!"
print (message)

