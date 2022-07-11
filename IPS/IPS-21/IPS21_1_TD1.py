fo = open('data.txt','w+')
for i in range (0,4):
    d = input()
    fo.write(d + "\n")

fo.close()

fo = open('data.txt','r+')
r = fo.readlines()
fo.close()
print (len(r))
a = 0
for i in r:
    l = i.split(' ')
    a = a + len(l)
print(a)
b = 0
c = 0
for i in r:
    i = i[:-1]
    l = i.split(' ') 
    for j in l:
        if j.isalpha():
            c = c + 1
        elif j.isnumeric():
            b = b + 1
print(b)
print(c)

