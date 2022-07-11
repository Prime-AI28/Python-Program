N = int(input())
if N > 0:
    l = []
    for i in range(0,N):
        na = input()
        name = str.lower(na)
        l.append(name)
    for i in range(0,len(l)):
        for j in range(i+1, len(l)):
            if l[j]<l[i]:
                t = l[j]
                l[j] = l[i]
                l[i] = t
            else: 
                pass
    for i in l:
        print(i.capitalize())