# creating a text file#
# 16.11.2022
# KingBoss aka RonsTechHub


# create text file
myfile = open("ronstechhub.txt","a")		# w for write, a for append
myfile.write("\n18.11.2022 - 23:23")
myfile.close()

textfile = open("ronstechhub.txt","r")
allcontent = textfile.read()
print(allcontent)