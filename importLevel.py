import string
from ctypes import windll
import os
import shutil


#SETTING

importLevelpath = "./ImportLevel" #edit if you want

#SETTING END

#DON'T EDIT THE CODE BELOW IF YOU DIDN'T KNOW WHAT ARE YOU DOING!



mode = ""

replaceid = ""

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

all_drives = get_drives()

valid = False

chosen_drive = "None"

while valid == False:

    userselectmode = input("Choose your mode(easy/advanced/help): ")

    if userselectmode == "help":

        print("\nCustomize: Enter your own steam workshop level id (If you don't know what is level id,please check our original github)\n")

    elif userselectmode == "easy":

        replaceid = input("Enter your own id: ")

        valid = True

    elif userselectmode == "advanced":

        replaceid = input("Enter your own id: ")

        validtwo = False

        while validtwo == False:

            finalprint = "\nChoose the drive contain steam: "

            for drive in all_drives:

                finalprint = finalprint + str(drive) + ","

            print(finalprint)

            chosen_drive = input("Enter: ")

            if chosen_drive in all_drives:

                validtwo = True

        valid = True


for drive in all_drives:

    if chosen_drive == "None":

        chosen_drive = str(drive)

    steampath = str(chosen_drive) + ":/" + "Program Files (x86)/Steam/steamapps/workshop/content/977950"

    isthere = os.path.isdir(steampath)

    if isthere == True:

        print("Found ADOFAI dummy level file!\n")

        isthereDummylevel = os.path.isdir(str(chosen_drive) + ":/" + "Program Files (x86)/Steam/steamapps/workshop/content/977950/" + str(replaceid))

        if isthereDummylevel == True:

            shutil.rmtree(str(chosen_drive) + ":/" + "Program Files (x86)/Steam/steamapps/workshop/content/977950/" + str(replaceid))

        else:

            print("\nInvalid id.You didn't subscribed to that level on steam! Run the script again!")

            break

        importLevelarray = os.listdir(importLevelpath)
        
        if importLevelarray == []:

            print("\nNo folder in 'ImportLevel'.Please run the script again!")

            break

        importLevel = importLevelarray[0]

        

        os.rename("./ImportLevel/" + str(importLevel),steampath + "/" + str(replaceid))

        print("Imported level!")

        break

    else:

        print("\nCannot found ADOFAI dummy level file!")
