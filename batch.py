# Batch rename
# Kevin Tam - version 0.1

import os

def userPrompt():

    while True:
        namePrompt = input("What would you like to name the file?\n")
        fileExtensionPrompt = input("What is the file extention?\n")
        startFileNumber = input("What number would you like to start at?\n")
        file_number = int(startFileNumber)

        renamedFile = namePrompt + startFileNumber + fileExtensionPrompt

        #confirmation if naming of the file is correct
        print("\n" + renamedFile + "\n")
        confirmation = input("Confirm if this is correct? Yes or No\n")

        if confirmation.lower() == "yes":
            os.chdir("path") #current working directory
            file_name = os.getcwd()

            for files in sorted(os.listdir(str(file_name))):
                renamed_file = os.rename(files, namePrompt + str(file_number) + fileExtensionPrompt)
                file_number += 1
                print(file)

if __name__ == '__main__':
    userPrompt()

