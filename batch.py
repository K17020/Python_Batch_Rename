import os

def userPrompt():

    while True:
        namePrompt = input("What would you like to name the file?\n")
        fileExtensionPrompt = input("What is the file extention?\n")
        startFileNumber = input("What number would you like to start at?\n")
        file_number = int(startFileNumber)

        renamedFile = "\n" + namePrompt + startFileNumber + fileExtensionPrompt + "\n"



        #confirmation if naming of the file is correct
        print(renamedFile)
        confirmation = input("Confirm if this is correct? Yes or No\n")

        if confirmation.lower() == "yes":
            os.chdir("C:/Users/HTPC/Downloads/DBZ Season 3") #current working directory
            file_name = os.getcwd()

            for files in os.listdir(str(file_name)):
                print(files[1])


        # renamed_file = os.rename(files, "Dragon Ball Z S02E0"+ str(file_number) + ".mkv")
        # file_number += 1

if __name__ == '__main__':
    userPrompt()
