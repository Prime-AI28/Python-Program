def bill(a):
    b = 0
    if a<=100:
        b = 0
    elif a<=200:
        b = 0 + (a-100)*1.5 + 20
    elif a<=500:
        b = 0 + (100 * 2) + (a-200) * 3 + 30
    else:
        b = 0 + (100*3.5) + (300*4.6) + (a-500) * 6.6 + 50
    return b

N = int(input())

fo = open('electric.txt','w+')
for i in range(0,N):

    name = input()
    con_num = input()
    units = int(input())
    pay = int(bill(units))
    fo.write(name + '  ' + con_num + '  '+ str(units) +'  '+ str(pay) + '\n')

fo.close()

fo = open('electric.txt','r+')
for i in range(0,N):
    read = fo.readline()
    data = read.split('  ')
    amount = int(data[3])
    if amount > 1000:
        print(read)
fo.close()