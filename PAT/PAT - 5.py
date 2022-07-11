import re
uid = input()
upd = input()
cap = input()

if re.match("^[21].*[BPS|BCE|BPI]{3}[0-9]{4}$",uid):
    if re.match("^[0-9]{2}[a-zA-Z]{3}$",upd):
        if re.match("^[A-Za-z]{2}[0-9]{1}[A-Z]{1}[0-9]{1}[A-Z]{1}",cap):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")