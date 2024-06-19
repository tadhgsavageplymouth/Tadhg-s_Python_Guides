# Tuples are immutable lists. Their values cannot be changed.
# They differ in syntax by using standard brackets instead of square brackets like in lists

# Lets create a tuple for the dimensions of a rectangle
dimensions = (200, 500)
print (dimensions[0])
print (dimensions[1])

# Tuples with only one element must include a trailing comma 
people = (1,)
print (people)

# Tuples may also be looped through as they are in lists
for dimension in dimensions:
    print(dimension)

# Although Tuples can't be modified they can be written over by redefining them
co_ordinates = (50, 100)
print ("\nThis is my orginal tuple:")
print (co_ordinates)

# co-ordinates being redefined and thus making tuples modifiyable 
co_ordinates  = (120, 200)
print ("\nThis is now the re-defined tuple:")
print (co_ordinates)


