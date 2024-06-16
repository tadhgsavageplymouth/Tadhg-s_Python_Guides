### Making a list of invities and an inviting message to each individual

invities = ["albert", "susan", "jason", "anne"]

message_1 = f"Hi, {invities[0].title()}, welcome to the party!"
message_2 = f"Hi, {invities[1].title()}, welcome to the party!"
message_3 = f"Hi, {invities[2].title()}, welcome to the party!"
message_4 = f"Hi, {invities[3].title()}, wlecome to the party!"

### Printing each new message with the seperator of a new line
print (message_1, message_2, message_3, message_4, sep="\n")

### New print message for Albert who can now not make it 
print (f"Sorry guys, {invities[0].title()}, cant make it!")

### Modifying list replacing albert with someone new who can make it 
### Deleting Albert from the list
del invities[0]

### Inserting Dan into the list at index 0
invities.insert(0,"dan")

### Appending a new person to the invities
invities.append("jim")

### Printing a new set of invites for each individual 

message_1 = f"Hi, {invities[0].title()}, welcome to the party!"
message_2 = f"Hi, {invities[1].title()}, welcome to the party!"
message_3 = f"Hi, {invities[2].title()}, welcome to the party!"
message_4 = f"Hi, {invities[3].title()}, welcome to the party!"
message_5 = f"Hi, {invities[4].title()}, welcome to the party!"

print (message_1, message_2, message_3, message_4, message_5, sep = "\n")


### Print statement to inform people that we have a bigger table and more guests are coming to dinner
print ("Hey guys we have a larger table and more guests are now coming to diner")

### Insertion of more guests into the list of invities 
print (invities)

invities.insert(0,"sally")
invities.insert(1,"alice")
invities.insert(2,"tom")
invities.append("derek")

print (invities)

### Printing a new set of invites for each individual 

message_1 = f"Hi, {invities[0].title()}, welcome to the party!"
message_2 = f"Hi, {invities[1].title()}, welcome to the party!"
message_3 = f"Hi, {invities[2].title()}, welcome to the party!"
message_4 = f"Hi, {invities[3].title()}, welcome to the party!"
message_5 = f"Hi, {invities[4].title()}, welcome to the party!"
message_6 = f"Hi, {invities[5].title()}, welcome to the party!"
message_7 = f"Hi, {invities[6].title()}, welcome to the party!"
message_8 = f"Hi, {invities[7].title()}, welcome to the party!"
message_9 = f"Hi, {invities[8].title()}, welcome to the party!"

print (message_1, message_2, message_3, message_4, message_5, message_6, message_7, message_8, message_9, sep = "\n")

print ("Sorry guys I can now only invite two people to dinenr!")

### In order to pop the last invitie you must use -1 to indicate last and not pop index number 8
popped_invitie = invities.pop(-1)
invities.pop(-1)

print (f"Sorry, {popped_invitie}!")

popped_invitie = invities.pop(6)
print (f"sorry, {popped_invitie}!")

popped_invitie = invities.pop(5)
print (f"Sorry, {popped_invitie}!")

popped_invitie = invities.pop(4)
print (f"Sorry, {popped_invitie}!")

popped_invitie = invities.pop(3)
print (f"Sorry, {popped_invitie}!")

popped_invitie = invities.pop(2)
print (f"Sorry, {popped_invitie}!")

print (invities)

print (f"Hi, {invities[0].title()}, I look forward to seeing you at the party!")
print (f"Hi, {invities[1].title()}, I look forward to seeing you at the party!")

del invities[1]
del invities[0]

print (invities)

# Printing total amount of invities
print (len(invities))

# Printing message with total amount of invities coming to dinner
print (f"The total amount of poeple coming to dinner is {len(invities)}.")

# List of countries 
countries = ["italy", "england", "ireland", "switzerland"]

# List of countries with formatting 
print (countries[0].title(), countries[1].title(), countries[2].title(), countries[3].title(), sep=", ")

# Reversing the order of the list
countries.reverse()
print (countries)
# Putting them back in original order
countries.reverse

# Temoparily sorting them
print (sorted(countries))

# Reversing the sorting mehtod
print (sorted(countries, reverse=True))
# Print original list
print (countries)

# Printing length of list
print (len(countries))

# Permanetly sorting
countries.sort()
print (countries)

# Reverse permanet sorting
countries.sort(reverse=True)
print (countries)

# Removing country in list
countries.remove("italy")
print (countries)

# Appending Italy back in
countries.append("italy")
print (countries)

# Deleting Switzerland from the list
del countries[0]
print (countries)

# Inserting Switzerland at index 0
countries.insert(0, "switzerland")
print (countries)

# Popping switzerland out and placing it in visted 

vistited = countries.pop(0)

countries.pop(0)

print (vistited.title())
print (countries)










