y = int(input())
def prod(a):
    if a<=3:
        return a
    else:
        return (prod(a-1)+prod(a-2)+prod(a-3))
if y>0:
    for i in range(1, y+1):
        print(prod(i),end=' ')
else:
    print("Invalid Input")