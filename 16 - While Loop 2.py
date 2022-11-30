# while loop program
# 13.11.2022.
# KingBoss aka RonsTEchHub


# ask the user for input
userinput = input("Please enter your user name.....")
print(userinput)

# keep asking until they enter the correct value
while userinput != "RonsTechHub":
    userinput = input("Silly human that is incorrect, try again.....")
    if userinput == "RonsTechHub":
        print("Human, you are not so silly afetrall.")
        
# when they enter the correct value, thank them
