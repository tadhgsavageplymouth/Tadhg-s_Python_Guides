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
my_pastas = ["Penne", "Fusili", "Farfalla", "Linguine"]

# Copying my list to my frends list
friends_pastas = my_pastas.copy()

# Printing my friends pasta
print (friends_pastas)

# Adding a new item to my pasta list
my_pastas.insert(0, "spaghetti")
print (my_pastas)

# Adding a new item to friends pasta list that is not in mine 
friends_pastas.append("tagletelle")
print (friends_pastas)

# Looping through to print list of my favourite foods 
print ("This is my food list:")
for my_pasta in my_pastas:
    print (my_pasta)

# Looping through to show my freidns favourite foods
print ("\nMy freinds fevouroite foods are:")
for friends_pasta in friends_pastas:
    print (friends_pasta.title())











