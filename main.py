import os
import re

#SETTING

path = "./OldVersion/" #edit to your own path if you want

outputpath = "./Output/" #edit to your own path if you want

#SETTING END

#DO NOT CHANGE THE CODES BELOW IF YOU DON'T KNOW WHAT ARE YOU DOING!

dir_list = os.listdir(path)

outputpathdir = os.listdir(outputpath)

ReplaceFalseWith = '"Disabled"'
ReplaceTrueWith = '"Enabled"'
ReplaceNullWith = "0"

for file in outputpathdir:


  success = False
  while success == False:
    ans = input("There is a file inside the output folder.Continue this program will cause the file to be overwritten.Are you sure?(y/n)\n")
    if ans == "y":

      os.remove(outputpath+str(file))
      
      success = True

    elif ans == "n":
      
      print("Program will not continue\n")
      success = False

valid = False

while valid == False:

  userversion = input("Please enter the version you want to replace: ")             

  if int(userversion) > 0:
    valid = True

  else:

    print("Version cannot be smalle than 0.Please type again!\n")

for file in dir_list:
  
  openfile = open(path + str(file),"r")
  
  
  lines = openfile.readlines()
  open(outputpath + str(file),"x")
  
  for line in lines:

    finallinewrite = line
    
    EnabledWrite = True

    if "version" in line:
      number = re.findall(r'\d+', finallinewrite)[0]
      
      finallinewrite = finallinewrite.replace(number, userversion)

      EnabledWrite = False
    
    
    if "legacyFlash" in line or "legacyCamRelativeTo" in line or "legacySpriteTiles" in line or "legacyTween" in line:
      EnabledWrite = False

    if EnabledWrite == True:
      
      if "false" in line:
        finallinewrite = finallinewrite.replace("false",ReplaceFalseWith)
      
      if "true" in line:
        finallinewrite = finallinewrite.replace("true",ReplaceTrueWith)

      if "null" in line:
        finallinewrite = finallinewrite.replace("null",ReplaceNullWith)
        
    with open(outputpath + str(file),"a") as newfile:
      newfile.write(finallinewrite)

print("Convert complete! File saved in: " + outputpath)
