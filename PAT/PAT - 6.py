def Tax(s,g):
    net = 0

    if g == 'Male':
        net = TaxMale(s)
    elif g == 'Female':
        net = TaxFemale(s)
    
    print(int(net))

def TaxMale(a):
    if a<=250000:
        b = 0
    elif a>250000 and a<=500000:
        b = 0 + (a-250000)*5/100
    elif a>500000 and a<=1000000:
        b = 0 + (250000)*5/100 + (a-500000)*20/100
    else:
        b = 0 + 250000*5/100 + 500000*20/100 + (a-1000000)*30/100
        
        return b

def TaxFemale(a):
    if a<=250000:
            b = 0
    elif a>250000 and a<=500000:
        b = 0 + (a-250000)*5/100
    elif a>500000 and a<=1000000:
        b = 0 + (250000)*5/100 + (a-500000)*10/100
    else:
        b = 0 + 250000*5/100 + 500000*10/100 + (a-1000000)*20/100
        
        return b

sal = int(input())
gen = input()

Tax(sal,gen)