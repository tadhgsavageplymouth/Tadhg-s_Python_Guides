# Making a new list 
countries = ["UK", "Italy", "Spain", "France", "Belgium"]
# Lets now just selectivley print the first 3 countries
print ("The first three countries are:")
print (countries[:3])

# Now lets just print the middle three countries
print ("the middle three countries are:")
print (countries[1:4])

# Now lets just print the last three countries
print ("The last three countries are:")
print (countries[-3:])

# Producing a quick list loop comprehension
countries = ["japan", "korea", "china"]
for country in countries:
    print (country)

# Producing a quick list comprehension
squares = [digits ** 2 for digits in range(1, 10)]
print (squares)

# My list of pasta 
my_pasta = ["Penne", "Fusili", "Farfalla", "Linguine"]

# Copying my list to my frends list
friends_pasta = my_pasta.copy()

# Printing my friends pasta
print (friends_pasta)

# Adding a new item to my pasta list
my_pasta.insert(0, "spaghetti")
print (my_pasta)

# Adding a new item to friends pasta list that is not in mine 
friends_pasta.append("tagletelle")
print (friends_pasta)

# Looping through to print list of my favourite foods 
print ("This is my food list:")
for food in my_pasta:
    print (food)

# Looping through to show my freidns favourite foods
print ("\nMy freinds fevouroite foods are:")
for f_foods in friends_pasta:
    print (f_foods.title())
    







