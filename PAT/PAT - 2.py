Y = int(input())

l=[0,1]

c=1

if (Y>0):
    print(l[1],end=' ')

    while (c!=Y):

        for i in range (0,Y-1):

            d= l[i]+l[i+1]

            print(d,end=' ')

            l.append(d)

            c=c+1

else:

    print('Invalid Input')