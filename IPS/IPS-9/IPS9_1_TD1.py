N=int(input())
if N>0:
    l=[]
    for i in range (0,N):
        price = int(input())
        l.append(price)
    print(sum(l)) 
else:
    print("Invalid Input")