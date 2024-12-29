import string
from ctypes import windll
import os
import shutil

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

while valid == False:

    userselectmode = input("Choose your mode(customize/help): ")

    if userselectmode == "help":

        print("\nCustomize: Enter your own steam workshop level id (If you don't know what is level id,please check our original github)\n")

    elif userselectmode == "customize":

        replaceid = input("Enter your own id: ")

        valid = True

for drive in all_drives:

    steampath = str(drive) + ":/" + "Program Files (x86)/Steam/steamapps/workshop/content/977950"

    isthere = os.path.isdir(steampath)

    if isthere == True:

        print("Found ADOFAI game file!\n")

        isthereDummylevel = os.path.isdir(str(drive) + ":/" + "Program Files (x86)/Steam/steamapps/workshop/content/977950/" + str(replaceid))

        if isthereDummylevel == True:

            shutil.rmtree(str(drive) + ":/" + "Program Files (x86)/Steam/steamapps/workshop/content/977950/" + str(replaceid))

        else:

            print("\nInvalid id.You didn't subscribed to that level on steam! Run the script again!")

            break

        importLevelpath = "./ImportLevel"

        importLevelarray = os.listdir(importLevelpath)
        
        if importLevelarray == []:

            print("\nNo folder in 'ImportLevel'.Please run the script again!")

            break

        importLevel = importLevelarray[0]

        

        os.rename("./ImportLevel/" + str(importLevel),steampath + "/" + str(replaceid))

        print("Imported level!")

        break

    else:

        print("\nCannot found ADOFAI game file!")
