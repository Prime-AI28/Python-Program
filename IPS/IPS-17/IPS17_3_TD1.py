n = int(input())

def fact(x):
    if x == 1:
        return 1
    else:
        return (x * fact(x-1))
        
if n<= 0:
    print("Invalid Input")
else:
    print(n)
    print(fact(n))