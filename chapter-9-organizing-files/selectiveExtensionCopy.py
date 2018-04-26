#! python3
#selectiveExtCopy.py - Walk through a folder tree and search for files with a
#                   cetain file extension and copy them to a new folder.

import os, shutil
# Walk through a folder tree
userFolder = r'C:\Users\HiewS\AppData\Local\Programs\Python' #-folder to be walked
copyDestination = r'C:\Users\HiewS\Desktop\selectiveExtCopy'
number = 1
# Check if the copyDestination is non-existant
while True:
    # If exist, then add a number behind it, repeat till doesn't exist.
    finalCopyDestination = copyDestination + '_' + str(number)
    number = number + 1
    # If not exist, then exit loop
    if not os.path.isdir(finalCopyDestination):
        os.mkdir(finalCopyDestination)
        break

for folder, subfolders, files in os.walk(userFolder):

# Go through the list and check if it ends with fileExtension
    for file in files:
        if file.endswith('.txt'):
# TODO: If it matches, join it together with the folder path and copy the file to
#       destination location using copy2.
            try:
                shutil.copy2(os.path.join(folder, file), finalCopyDestination)
            except PermissionError:
                print(os.path.join(folder, file) + 'is not copied.')
            
# Skip those which doesn't.
        else:
            continue
# TODO: When completed, print "Done."
print('Done.')
