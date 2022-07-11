def compute(f,n):
    a = lambda x: x**2 if f==1 else x**3
    print(a(n))
    
flip = int(input())
num = int(input())

if flip == 1 or flip == 2:
    compute(flip,num)
else:
    print("Invalid Input")