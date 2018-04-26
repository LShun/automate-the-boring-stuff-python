#regexVersionOfStrip().py -strips "replaceChar" from a string

import re
passedStrip = '     HI        IM M      ARK             '
def RegStrip(inputStrip, replaceChar):
  if replaceChar == '':
    frontSpaceDetector = re.compile(r'^\s*')
    backSpaceDetector = re.compile(r'\s*$')
    frontStripped = frontSpaceDetector.sub('', inputStrip)
    backAndFrontStripped = backSpaceDetector.sub('', frontStripped)
    print(backAndFrontStripped)
  elif replaceChar != None:
    frontSpaceDetector = re.compile(replaceChar)
    frontStripped = frontSpaceDetector.sub('', inputStrip)
    print(frontStripped)
    
RegStrip(passedStrip, 'H')
    
    
  
