N = int(input())
if (N<1):
    print("Invalid Input")
elif(N==1):
    print("Not a Prime")
elif (N==2):
    print(2)
else:
    for i in range (0,N+1):
        if i>1:
            for j in range (2,i):
                if (i%j==0):
                    break
            else:
                print(i)
            
            
            