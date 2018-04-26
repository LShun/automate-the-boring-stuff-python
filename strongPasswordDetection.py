import re
def passwordDetection(password):
  if passwordTotalAlgo.search(password) == None:
    print('False')
  elif passwordAtLeastOneNum.search(password) == None:
    print('False')
  elif passwordAtLeastOneCap.search(password) == None:
    print('False')
  elif passwordAtLeastLower.search(password) == None:
    print('False')
  else:
    print('True')
  

passwordTotalAlgo = re.compile(r'''(
(.{8,})   # at least 8 characters
)''', re.VERBOSE)

passwordAtLeastOneNum = re.compile(r'''(
(\d+)
)''', re.VERBOSE)

passwordAtLeastOneCap = re.compile(r'''(
([A-Z]+)
)''', re.VERBOSE)

passwordAtLeastLower = re.compile(r'''(
([a-z]+)
)''', re.VERBOSE)

print('Password Strength Verification ( true if strong, false if not ), please type in a password:')
inputPassword = input()
passwordDetection(inputPassword)
