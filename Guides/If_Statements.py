# Tetsing for inequality
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


