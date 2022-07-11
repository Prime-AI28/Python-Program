def GetName(l1):
    a = input()
    l1.append(a)
    return l1
def sortName(l1, nop):
    for i in range (0,nop):
        for j in range(0,nop):
            if l1[i] < l1[j]:
                temp = l1[i]
                l1[i] = l1[j]
                l1[j] = temp
    return l1

n_p = int(input())
l_p = []
if n_p > 0:
    for i in range(0,n_p):
        l_p = GetName(l_p)
    l_o_p = sortName(l_p , n_p)
    for i in range (0,n_p):
        print(l_o_p[i])    
else:
    print("Invalid Input")