N=int(input())

if (N>0):
    s=10**10
    s2=10**10
    for i in range (0,N):
        x=int(input())
        
        if (x<s):
            s,s2=x,s
        elif (x<s2):
            s2=x
    print("Second Smallest Number is" ,s2)
else:
    print("Invalid Input")
