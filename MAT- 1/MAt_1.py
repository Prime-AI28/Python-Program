v = int(input())
f = int(input())
g = int(input())

if v>0 and f>0 and g>0:
    veg_list = []
    frt_list = []
    gry_list = []
    
    for i in range(0,v):
        veg = input()
        veg_list.append(veg)
    
    for i in range(0,f):
        frt = input()
        frt_list.append(frt)
    
    for i in range(0,g):
        gry = input()
        gry_list.append(gry)
        
    
    veg_list.sort()
    frt_list.sort()
    gry_list.sort()
    
    Item_list = veg_list + frt_list + gry_list
    
    Item_sort_list = sorted(Item_list)
    
    for i in Item_list:
        print(i, end='')
    for j in Item_sort_list:
        print(j, end='')
    
else:
    print("Invalid Input")
