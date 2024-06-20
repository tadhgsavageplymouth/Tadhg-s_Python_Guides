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

    

    
