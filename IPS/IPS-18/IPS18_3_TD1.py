def order(a):
    x = lambda z: z.sort()
    x(a)
    for i in range(0,n):
        print(a[i])
    
n = int(input())
l = []
if n>0:
    for i in range(0,n):
        name = input()
        l.append(name)
    order(l)
else:
    print("Invalid Input")