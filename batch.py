# Batch rename 
# Kevin Tam - version 0.1

import os

file_number = 1

os.chdir("name_of_directory") #current working directory
file_name = os.getcwd()

for files in os.listdir(str(file_name)):
    renamed_file = os.rename(files, "The_name_of_the_file"+ str(file_number) + ".txt")
    file_number += 1
