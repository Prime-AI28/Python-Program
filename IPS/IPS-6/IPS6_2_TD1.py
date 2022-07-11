x=int(input())
old = x
sum = 0
if x>0 and x<10:
    print('Do nor enter single digit')
elif x<=0:
    print('Invalid Input')
else:
    while(x>=1):
        t = x%10            #remainder, extract individual digit
        c = t**3            #cube of individual digit
        sum = sum + c       #sum of cube of individual digit
        x = x//10           #to drop a digit
    if old == sum :
        print('Equal')
    else:
        print ('Not Equal')