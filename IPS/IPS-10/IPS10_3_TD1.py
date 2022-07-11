N = int(input())

if N>0:
    g1 = []
    g2 = []
    g3 = []

    for i in range (0,N):
        age = int(input())
        
        if age<1:
            print("Invalid Input")
            quit()
        elif 0<age<11:
            g1.append(age)
        elif 10<age<61:
            g2.append(age)
        elif 60<age:
            g3.append(age)

    print("Group 1 count",len(g1))
    print("Group 2 count",len(g2))
    print("Group 3 count",len(g3))

    print("Group 1 average",sum(g1)/len(g1))
    print("Group 2 average",sum(g2)/len(g2))
    print("Group 3 average",sum(g3)/len(g3))
else:
    print("Invalid Input")
    