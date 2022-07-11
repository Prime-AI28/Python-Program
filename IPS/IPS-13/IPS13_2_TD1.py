import re
e = input()
if re.match("[A-Za-z0-9]*[@]{1}.*[.com|.in|.org|.edu|.net|.mil]",e):
    print('Valid')
else:
    print('Invalid')