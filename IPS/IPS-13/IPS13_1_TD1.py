import re
pan = input()

if len(pan) == 10 and re.match("[A-Z]{5}[0-9]{4}[A-Z]{1}",pan):
    print('Valid')
else:
    print('Invalid')