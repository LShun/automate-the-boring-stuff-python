#! python3
# UnneededFileNames.py - Find all exceptionally large files and print these files with their absolute path to the screen.
import os
# TODO: Walk through a certain folder
print('Big File Finder')
print('Please input your folder location to find for extra large files:')
folderLocation = r'/'

print('Checking the path:' + folderLocation + 'for files above 100MB')
for folder, subfolders, files in os.walk(folderLocation): # walk through the folder
  for i in files:
    possibleFileLocation = os.path.join(folder, i)
    fileSize = os.path.getsize(possibleFileLocation) / (1024*1024) # get the filesize of all individual files
    if fileSize >= 100: # If it is above 100MB, display it on screen
      print(possibleFileLocation + 'is equal or bigger than 100 MB'):
    else:
      continue
    
print('Done.')
