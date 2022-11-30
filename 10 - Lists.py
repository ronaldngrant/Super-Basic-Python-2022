# list program
# 12.11.2022
# Creator: RonsTechHub

# create a list of four items
names = ["RonsTechHub","TechJamo","RaeMo2Hands","IGN"]

# get the length of the list
print("Length Of List:",len(names))

# print original list
print("\nOriginal List:",names)

# prove it is a list - type()
print("\nType Of Data:",type(names))
print(type(names))

# append an item to the list
names.append("Bob The Builder")
names.append("Goku")
names.append("Majin Buu")

# print updated list
print("\nUpdated List:",names)

# remove an item from a list
names.remove("Goku")
print("\nLsit After Remove:", names)

# get the length of the list
print("\nLength Of List:",len(names))

# sort the list - same datatype
names.sort()
print("\nLsit After Sort:", names)

# sort in the opposite direction (descending)
names.sort(reverse=True)
print("\nLsit After Reverse:", names)

# list with multiple data types
newlist = ["Bob", 10, "Person A", 200]
print(newlist)

# join two lists
jointlist = newlist+names
print("\n\n\nJoint List Contents",jointlist)
