# Lets create a list of names and the slice the list for a temoprary output 
names = ["Dan", "James", "Kiton", "Matt"]
print (names[0:2])

# Printing starting at the first index of the list by ommiting the first index number
names = ["Dan", "James", "Harry", "Dion"]
print (names[:3])

# Simmilar indexing protocols work if you want to omit the begining of the list and have the last of it
names = ["Dion", "James", "Matt", "Bea", "Gerry"]
print (names[3:])

# Using a negative index to output the last of a list starting at an index
name = names
print (names[-2:])

# A third value can be placed in the brackets too to indicate a skip value
names = names
print (names[0:5:2])

# Lets now loop through a slice to print only three players with a sentence as part of a team
players = ["Dan", "Harry", "Jason", "Dion", "Jimmy", "Henry", "James"]
print ("Here are the first three players on the team: ")
for player in players [:3]:
    print (player.title())

# Copying lists 
my_food = ["pizza", "pasta", "bacon", "eggs", "salami"]

friends_food = my_food[:]

print ("My favourite food are:")
print (my_food)

print ("\nMy freinds favourite foods are:")
print (friends_food)

my_food.append("cheese")
print (my_food)
print (friends_food)

# In many occasions it might be better to use the copy method as it is more explicit

cars = ["Bugatti", "Ford", "volkswagen", "ferarri"]
# Using the copy method to make a new list explicitly
new_cars = cars.copy()
# Printing both out 
print(cars)
print(new_cars)

old_cars = cars[:]
print(old_cars)


retro_cars = cars.copy()
retro_cars.append("citroen")
print (retro_cars)
print (cars)

