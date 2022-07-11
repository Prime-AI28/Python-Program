def div7(N):
    l = []
    for i in range (1,N):
        if i%7 == 0:
            l.append(i)
    return l
N = int(input())
if N>0:
    ans = div7(N)
    for i in ans:
        print(i,end = " ")
else:
    print("Invalid Input")