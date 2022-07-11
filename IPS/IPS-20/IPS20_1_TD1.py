N = int(input())
fo = open("hospital.txt",'w')
for i in range(0,N):
    name = input()
    age = input()
    reason = input()
    fo.write(name + ' '+ age + ' ' + reason + ' ' + "\n" )
fo.close()

fo = open('hospital.txt','r')

for j in range (0,N):
    
    read = fo.readline()
    l = read.split(' ')
    if l[2] == 'Fever' or l[2] == 'fever':
        for i in range (0,3):
            print(l[i],end=' ') 
fo.close()

