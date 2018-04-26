#!python3
#fillingInTheGaps.py -  Find all files with a given prefix in a single folder
#                       and locate any gaps in the numbering. Then, have the
#                       program rename the filenames which are out-of-order.

import os, re, shutil

def fillingInTheGaps(prefix, extension, insertGapNumber):
    print('Prefix is: ' + prefix ) # prefix for use in checking
    print('Extension is: ' + extension ) # extension for use in checking
    print('Checking the directory: ' + folderLocation ) # status message
    # List the folder contents
    folderContents = sorted(os.listdir(folderLocation))
    matchFiles = [] # List to store matched values later
    for i in folderContents:
        if i.startswith(prefix):
    # If file with prefix found, store it in a list.
            matchFiles.append(i)
        else:
            continue # otherwise continue with the next iteration.
    digitFinder = re.compile(r'\d+')
    digitFinderResults = digitFinder.search(str(matchFiles))
    totalDigitLength = '{:0' + str(len(digitFinderResults[0])) +'d}'
    for number, file in enumerate(folderContents):
        #print(f'{file} should be number {number}')
        if number >= int(insertGapNumber):
            originalFilePath = os.path.join(folderLocation, file)
            editedFilePath = os.path.join(folderLocation, prefix + str(totalDigitLength.format(number + 1)) + extension)
            shutil.move(originalFilePath, editedFilePath)
        elif file == prefix + str(totalDigitLength.format(number)) + extension:
            continue
    #print("if it isn't, rename it")
        else:
            originalFilePath = os.path.join(folderLocation, file)
            editedFilePath = os.path.join(folderLocation, prefix + str(totalDigitLength.format(number)) + extension)
            shutil.move(originalFilePath, editedFilePath)

print('Fill In File Name Gaps & Add Gaps', ) # Sketchy title
print('''Input your folder location, the folder must be an absolute path and contain no subfolders''')
folderLocation = r'{}'.format(input()) # input folder location
folderLocation = os.path.abspath(folderLocation) # ensure it is an abstract path
print("Input a prefix to find for, for example: 'bear' without the ''")
userprefix = input()
print("Input an extension of a file type to find for, for example:'.txt' for notepad files")
userextension = input()
print("Do you want to insert a gap for a certain number? If yes, put a number, else, type '0' then press enter")
userinsertGapNumber = input()
fillingInTheGaps(userprefix, userextension, userinsertGapNumber) # modify the "prefix" - prefix of file , "extension" - extension of file
print('Done.')                               # and "insertGapNumber" - insert gap at which location 
