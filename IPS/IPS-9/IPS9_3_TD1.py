list1=["Apple", "Orange", "Mango", "Banana"]

list2=[120,100,85,50]

N = int(input())
if (N>0):
    sum=0
    lproduct = []
    lprice = []
    for i in range (0,N):
        
        product=input()
        if product in list1:
            lproduct.append(product)
            l = list1.index(product)
            lprice.append(list2[l])
            sum = sum + list2[l]
            
        else:
            print("Product not found")
            exit()
    print(sum)
else:
    print("Invalid Input")