fo = open('data.txt','w+')
for i in range (0,4):
    d = input()
    fo.write(d + "\n")

fo.close()

fo = open('data.txt','r+')
r = fo.readlines()
fo.close()

a = 0
e = 0
i = 0
o = 0
u = 0
for k in r:
    k = k[:-1]
    l = k.split(' ')
    for j in l:
        for m in j:
            if m == 'a':
                a = a+1
            elif m == 'e':
                e = e+1
            elif m == 'i':
                i = i+1
            elif m == 'o':
                o = o+1
            elif m == 'u':
                u = u+1
            
print("a is ",a)
print("e is ",e)
print("i is ",i)
print("o is ",o)
print("u is ",u)