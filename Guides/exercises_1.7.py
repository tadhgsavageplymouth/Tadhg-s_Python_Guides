# Making a buffet tuple
buffet = ("pasta", "bacon", "eggs", "ham", "chicken")
print (buffet)

# Using a for loop to print the foods in the buffet menu
print ("\nThese are the foods in the original buffet:")
for food in buffet:
    print (food.title())

# Lets now chage the items in the buffet
print ("\nHere is now the revised food list:")
buffet = ("pasta", "bacon", "eggs", "beef", "pizza")
for food in buffet:
    print (food.title())


