name = input()
m1 = int(input())
m2 = int(input())
m3 = int(input())
if m1>-1 and m2>-1 and m3>-1 and m1<=100 and m2<=100 and m3<=100:
    
    total = m1+m2+m3
    av = total/3
    
    fo = open("marks.txt",'w')
    fo.write(name+"\n"+str(m1)+'\t'+str(m2)+'\t'+str(m3)+'\n'+str(total)+'\n'+str(av))
    fo.close()

    fo = open('marks.txt','r')
    print(fo.read())
    fo.close

else:
    print("Invalid Mark")