# Batch rename 
# Kevin Tam - version 0.1

import os, shutil
#TODO add it so you can exit the program
#Add loop
print("Hello this program is designed to perform a batch rename of your files.")

print(os.getcwd() + " is your current working directory\n")

newFileName = raw_input("What would you like to name the file?\n")
fileFormat = raw_input("What is the file type?\n")

pwd = raw_input("Where are your files located? eg:(C:\ )\n")
os.chdir(os.getcwd() + pwd) #Change to this directory

#TODO add try and exceptions

#Loop through the file names
x = 0
for fileNames in os.listdir(os.getcwd()):	
	y = str(x)
	os.rename(fileNames,newFileName + "S0E" + y + fileFormat )
	x +=1

print(os.listdir(os.getcwd())) #List all the files in the current working directory
