paswrd = input()
upper = 0
lower = 0
num = 0
spcl = 0
l = len(paswrd)
if l>7 and l<16:
    for i in paswrd:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isnumeric():
            num += 1
        else:
            spcl += 1
    if upper>0 and lower>0 and num>0 and spcl>0:
        print('Valid')
    else:
        print('Invalid')
else:
    print("Invalid")
