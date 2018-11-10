# Batch rename 
# Kevin Tam - version 0.1

import os, shutil
#TODO add it so you can exit the program
#Add loop
print("Hello this program is designed to perform a batch rename of your files.")

print(os.getcwd() + " is your current working directory\n")

pwd = raw_input("Where are your files located? eg:(C:\ )\n")
#TODO add try and exceptions
print(os.chdir(os.getcwd() + pwd)) #Change to this directory

#Loop through the file names
x = 0
for fileNames in os.listdir(os.getcwd()):	
	y = str(x)
	os.rename(fileNames,"hello" + y + ".txt" )
	x +=1

print(os.listdir(os.getcwd())) #List all the files in the current working directory
