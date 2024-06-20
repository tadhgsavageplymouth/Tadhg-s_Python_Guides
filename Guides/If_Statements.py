# Tetsing for equality
# Lets create a list of cars, we want some in title case and some in upper
cars = ["toyota", "ford", "mercedes", "bmw", "ferrari"]
# Ussage of a for loop
for car in cars:
    # if statement used if bmw to print to upper
    if car == "bmw":
        print (car.upper())
    # Else statement used to print all other cars to title case
    else:
        print (car.title())
    

# Tetsing for case in python
car = "Audi"
# The lower method here would not change the value stored in the list. It would still be "Audi"
car.lower() == "audi"
print (car)

# Now lets learn to test for inequalites

requested_pizza = 'Diavola'
if requested_pizza != 'Diavola':
    print ('Dont send pizza!')
else:
    print ("send the pizza!")

cars = ["audi", "mercedes", "ford", "ferrari", "bmw"]
for car in cars:
    if car == ("bmw"):
        print (car.upper())
    else:
        print (car.title()) 

    
# Lets check for an inequality
pasta_dish = "carbonara"
if pasta_dish != "carbonara":
    print(f"Do not send the {pasta_dish.title()}!")
else:
    print(f"Send the {pasta_dish}!")


# Magic number guesser 
magic_number = 14
if magic_number != 20:
    print ("Not correct!")
else:
    print ("well done! You have guessed the numeber!")

# Age detector to pass bar using the keyword and 
person_A = 18
person_B = 18

if person_A >= 18 and person_B >= 18:
    print ("You may pass")
else:
    print("May not enter")

# Age detector based on the keyword or 

person_B = 16
person_A = 18

if person_A >= 18 or person_B >=18:
    print("You may pass")
else:
    print("Youmay not pass")

requested_toppings = ["mushrooms", "tomatoes", "bacon", "eggs"]
if "mushrooms" in requested_toppings:
    print (f"Yes, {requested_toppings[0]} is in the toppings")
else:
    print("No")
if "sausage" in requested_toppings:
    print ("Yes")
else:
    print ("No")

ingredients = ["eggs" , "pasta", "bread", "mushrooms"]
for ingredient in ingredients:
    print (ingredient)

if "mushrooms" in ingredients:
    print ("yes")

age_A = 18
age_B = 16

if age_A >= 21 in age_A:
    print ("yes")
else:
    print ("No")

ordered_pizza = "Diavola"
if ordered_pizza != "Diavola":
    print ("Not a diavola pizza")
else:
    print ("Diavola Pizza")


cars = "Audi"
car.lower() == "audi"

cars = ["audi", "bmw", "mercedes", "toyota", "honda"]
if car == "bmw":
    print (car.upper())
else:
    print (car.title())


if "bmw" in cars:
    print("True")
else:
    print (False)


user = "Anne"
banned_users = ["Jason", "Dan", "Elen", "Cassie"]
if user in banned_users:
    print (f"{user}, is banned")
else:
    print(f"{user}, is not banned")


cars = ["mercedes", "jaguar", "bmw", "ford", "ferrari"]
if car == "bmw":
    print(car.upper())
else:
    print(car.title())






