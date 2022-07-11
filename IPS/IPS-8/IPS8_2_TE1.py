x=int(input())
z=int(input())

if (x<0 or z<0) :
    print("Invalid Input")
else:
    t=0
    for i in range (1,z+1):
        t = t+x**i
    print(t)