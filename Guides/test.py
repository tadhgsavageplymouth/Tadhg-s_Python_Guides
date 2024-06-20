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


