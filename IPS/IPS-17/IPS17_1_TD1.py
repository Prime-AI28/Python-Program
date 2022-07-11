z = int(input())

rn = 0
def revnum(x):
    if (x>0):
        global rn
        rem = x%10
        rn = rn*10+rem
        x = x//10
        return (revnum(x))
    else:
        return rn

if z<1:
    print("Invalid Input")
elif z<10:
    print("Do not enter single digit")
    
else:
    print(revnum(z))