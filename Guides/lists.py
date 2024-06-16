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

### Removing an item using the del statement 
print (crisps)

del crisps[0]
print (crisps)


### Alternatibvley an item can be deleted using the pop method 
### This is a useful method that allows us to use the value of an item after it has been removed from the list.

### Creating a new list of crisps
crisps = ["walkers", "quavers", "lays", "sensations", "monster munch"]
print (crisps)

### Creating new variable and assigning it the value of the popped crisps
popped_crisps = crisps.pop()
print (crisps)
print (popped_crisps)

### Taking the popped value and placing it into a new list called "old crisps"

old_crisps = []
old_crisps.append(popped_crisps)
print (old_crisps)

### Using an f string to print a sentence with popped value 
print (f"My last bag of crisps were a packet of {popped_crisps}, I liked them very much!")

### Popping any item from the list using index in parenthesise 
crisps = ["walkers", "quavers", "lays", "monster munch"]
popped_crisps = crisps.pop(1)
print (popped_crisps.title())

### If the index position is unknown of the value you want to remove but the value is, use the remove method 

crisps = ["walkers", "lays", "quavers", "monster munch"]
crisps.remove("walkers")
print (crisps)

### Lets make a sentence using f string and the rmeove method 
### Making new list
crisps = ["walkers", "lays", "monster munch"]

### Assignining value too_expensive with monster munch
too_expensive = "monster munch"

### Removing the variable too expensive from the list
crisps.remove(too_expensive)

### Using f string to tie it all together and print with grammar and formatting
print (f"\nA packet of {too_expensive.title()} is too expensive for me")
print (crisps[0].title(), crisps[1].title(), sep = ", ")

### Use pop for index and remove for value 

### Create list of sweets
sweets = []

### Append new items to list
sweets.append("frutella")
sweets.append("starburst")
sweets.append("skittles")
sweets.append("refresher")

### Print new list of sweets
print (sweets)

### Pop last item into "eaten sweets" variable
eaten_sweets = sweets.pop(2)

sweets.pop(2)

print (eaten_sweets)
print (sweets)

### Creating new list utilising the remove function
chocolate = ["cadbury", "dairy milk", "fredo", "crunchie"]
print (chocolate)

### Usage of the del statement (only wroks on index not value)
del chocolate[1]
print (chocolate)

### Usage of the remove statement to remove a value 
chocolate.remove("cadbury")
print (chocolate)

### Repending old choclates back in
chocolate.append("cadbury")
chocolate.append("fredo")

print (chocolate)

### Using f strings to concatenate a sentence 
print (f"I like {chocolate[1].title()}, it truly is my favourite!")














