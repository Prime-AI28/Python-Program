N=int(input())
if (N>0):
    p=0
    n=0
    for i in range (0,N):
        x = int(input())
        if (x>0):
            p+=1
        else:
            n+=1
    print('Positive Numbers',p)
    print('Negative Numbers', n)
else :
    print('Invalid Input')