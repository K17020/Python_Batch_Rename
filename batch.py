# Batch rename
# Kevin Tam - version 0.1

import os
from natsort import natsorted

def userPrompt():

    while True:
        workingDirectory = input("What directory would you like to work in?\n")
        namePrompt = input("What would you like to name the file?\n")
        fileExtensionPrompt = input("What is the file extention?\n")
        startFileNumber = input("What number would you like to start at?\n")
        file_number = int(startFileNumber)

        renamedFile = namePrompt + startFileNumber + fileExtensionPrompt

        #confirmation if naming of the file is correct
        print("\n" + renamedFile + "\n")
        confirmation = input("Confirm if this is correct? Yes or No\n")

        if confirmation.lower() == "yes":
            os.chdir(workingDirectory.replace("\\","/")) #current working directory
            file_name = os.getcwd()
            
            for files in natsorted(os.listdir(str(file_name))):
                renamed_file = os.rename(files, namePrompt + str(file_number) + fileExtensionPrompt)
                print(files + "-->" + namePrompt + str(file_number) + fileExtensionPrompt)
                file_number += 1

if __name__ == '__main__':
    userPrompt()
