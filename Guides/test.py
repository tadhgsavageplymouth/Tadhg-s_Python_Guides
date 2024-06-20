cars = ["jaguar", "mercedes", "ford", "bmw", "audi"]
for car in cars:
    if car == "bmw":
        print (car.upper())
    else:
        print (car.title())

# For an equality
car = "Audi"
if car.lower() == "audi":
    print("True")
else:
    print("False")

# For inequality

car = "Audi"
if car.lower() != "audi":
    print(f"This is not an {car}")
else:
    print(f"This is an {car}")


# Guess the magic numeer
guess = 21
if guess == 20:
    print("Correct!")
else:
    print("Wrong!")

# Age Detector to pass into a bar
Age_A = 18
Age_B = 16

if Age_A == 18 and Age_B == 18:
    print("You may pass")
else:
    print("You may not pass")

if Age_A == 18 or Age_B == 18:
    print("You may pass")
else:
    print("You may not pass")

# Lets try again to copy and slice a list
cars = ["audi", "ford", "honda", "bmw", "toyota"]

old_cars = cars[0:2]    
print (old_cars)
print(cars)

new_cars = cars.copy()
new_cars.insert(0, "mercdes")

for new_car in new_cars:
    if new_car == "bmw":
        print(new_car.upper())
    else:
        print(new_car.title())



# Lets make 10 conditional tests
# Lets test if a word is in a sentence 
sentence = "The fox ran up the hill"
if "fox" in sentence:
    print ("True")
else:
    print(False)

# If the tempreture is lower that 20 degrees turn on heat, else turn on AC
temp = 25
if temp < 20:
    print ("Turn on the AC")
else:
    print("Turn on the heater")


# Raning and umbrella 
raining = True
umbrella = True
if raining and umbrella:
    print ("You may go for a walk")
else:
    print ("You may not go for a walk")


# Lets for another equality and inequality test
# This is an example of an equality
fruit = "Apple"
if fruit.lower() == "apple":
    print(f"This is an {fruit}")
else:
    print(f"This is not an {fruit}")

# Lets not do an example of an equality

age = 16
if age != 18:
    print("You may not come in")


# Test if item is in a list
cakes_in_stock = ["Victoria Sponge", "Mini Rolls", "Bakewell Tart", "Angel Slices"]
cakes_to_check = ["Victoria Sponge", "Mini Rolls", "Bakewell Tart", "Angel Slices"]

for cake in cakes_to_check:
    if cake in cakes_in_stock:
        print (f"{cake}, is in stock")
    else:
        print (f"{cake}, out of stock")









