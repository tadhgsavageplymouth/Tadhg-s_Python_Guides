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
    

