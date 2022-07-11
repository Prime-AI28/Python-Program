def fact(n):
    
    sum = 0
    for i in range (1,n+1):
        f = 1
        
        for j in range(1,i+1):
            f = f*j
        sum = sum + f
    return sum
N = int(input())
if N>0:
    ans = fact(N)
    print(ans)
else:
    print("Invalid Input")