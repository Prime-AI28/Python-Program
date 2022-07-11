n_d = int(input())

def fibo(x):
    if x <= 1:
        return x
    else:
        return (fibo(x-1)+fibo(x-2))
    
if n_d<1:
    print("Invalid Input")
else:
    for i in range(1,n_d+1):
        print(fibo(i),end=' ')