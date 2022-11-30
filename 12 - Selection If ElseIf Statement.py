# selection program
# 12.11.2022.
# KingBoss aka RonsTEchHub

# create a variable called “referenceage”
referenceage = 21

# get user input
userage = input("Please enter your age.....")
print(userage)
print(type(userage))

# convert it to a whole number
userage = int(userage)
print(type(userage))

if userage < referenceage:
    print("You are NOT able to drive.")
elif userage == referenceage:
    print("MAYBE you can drive.")
elif userage > referenceage:
    print("If you cannot drive you are lazy.")    
else:
    print("I dont know what is going on.")
