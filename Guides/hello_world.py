cakes_in_stock = ["Victoria Sponge", "Bakewell Tart", "Vanilla Swirl"]
cakes_to_check = cakes_in_stock
for cake in cakes_in_stock:
    if cake in cakes_in_stock:
        print(f"{cake} in stock")
    else:
        print(f"{cake}, out of stock")

if "Cherry Bakewell" in cakes_in_stock:
    print("Cherry Bakewell in stock")
else:
    print("Cherry bakewell not in stock")

# Using elif for ages for price at amusement park
age = 12
if age < 4:
    print ("You go free")
elif age < 18:
    print ("Price is 25 pounds")
else:
    print("You pay 40 pounds")


# Lets improve this to by adding the new variable price and one print statement 

age = 45
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 50
else:
    price = 10

print (f"Your addmission cost is £{price}")

# If elif and else statments are useful but sometime we want all tests to run. In such a sase just use if

pizza_toppings = ["peperoni", "mushrooms", "tomatoes", "cheese"]
if "peperoni" in pizza_toppings:
    print("Add peperoni")
if "mushrooms" in pizza_toppings:
    print("Add mushrooms")
if "tomatoes" in pizza_toppings:
    print("add tomatoes")
if "chorizo" in pizza_toppings:
    print("Add chorizo")
if "cheese" in pizza_toppings:
    print("Add cheese")
print("\nPizza finsihed!")






    
