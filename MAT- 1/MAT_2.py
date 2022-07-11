Fr=['Apple' , 'Banana' , 'Mango']

Veg=['Carrot' , 'Cabbage' , 'Potato']

Gro=['Wheat' , 'Sugar' , 'Rice']

Fprice=[100,50,80]

Vprice=[70,40,35]

Gprice=[45,55,50]

Item_list = Fr + Veg + Gro

N = int(input())

Items = []
Count = []


for i in range(N):
    Item_name = input()
    Items.append(Item_name)
    Item_count = float(input())
    Count.append(Item_count)

sum = 0
l = len(Items)
    
for i in range (0,l):
    if Items[i] in Fr:
        pos = Fr.index(str(Items[i]))
        val = Fprice[pos]
        weight = float(Count[i])
        s = val * weight * 0.95
        sum = sum + s
        
    elif Items[i] in Veg:
        pos = Veg.index(str(Items[i]))
        val = Vprice[pos]
        weight = float(Count[i])
        s = val * weight * 0.97
        sum = sum + s
            
    elif Items[i] in Gro:
        pos = Gro.index(str(Items[i]))
        val = Gprice[pos]
        weight = float(Count[i])
        s = val * weight * 0.93
        sum = sum + s
            
    else:
        print("Invalid Input")
        quit()
            
print(format(sum,".1f"))
    

