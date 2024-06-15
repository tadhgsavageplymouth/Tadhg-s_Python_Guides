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

### Modifying an element in a list
cars = ["Bugatti", "Honda", "Ford"]

### This replaces the item 1 with Ferrari instead
cars[1] = "Ferrari"

### Item then printed below
print (cars[1])

### Now lets print with title formatting too (seperator included in paranthesise and with comma)
print(cars[0].title(), cars[1].title(), cars[2].title() , sep =', ')

### Additing elements to a list 
### Here the append method is used after the list cars to add new info in
print (cars)
cars.append("ferrari")
print (cars)
### Printing last car in list
print (cars[-1].title())

### Lets create a new list starting from an empty list and adding new user information in using append
crisps = []
print (crisps)

crisps.append("walkers")
print (crisps[0].title())

crisps.append("lays")
print (crisps[0].title(), crisps[1].title(), sep = ", ")

crisps.append("monster munch")
print (crisps[0].title(), crisps[1].title(), crisps[2].title(), sep = ", ")

### Usage of the Insert method to insert new elements into a list
print (crisps)
crisps.insert(0, "quavers")
crisps.append("sensations")

### Printing of new list
print (crisps[0].title(), crisps[1].title(), crisps[2].title(), crisps[3].title(), crisps[4].title(), sep = ", ")



