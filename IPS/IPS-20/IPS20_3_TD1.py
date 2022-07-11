N = int(input())
fo = open("student.txt",'w')
for i in range (0,N):
    
    name = input()
    m1 = int(input())
    m2 = int(input())
    m3 = int(input())
        
    total = m1+m2+m3
    av = total/3   
    fo.write(name+' ' +str(m1)+' '+str(m2)+' '+str(m3)+' '+str(total)+' '+str(int(av)) + ' ' + "\n")
fo.close()

fo = open('student.txt','r')

for j in range (0,N):
    l = fo.readline().split(' ')
    av = int(l[5])
    for i in range(0,6):
        print(l[i],end=' ')
    print("\n")

fo.close()
