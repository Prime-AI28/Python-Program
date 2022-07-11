def compute(s,x,y):
    
    print(len(s))
    print(len(x))
    print(len(y))
    print(s.find(x))
    print(s.replace(x,y))


str = input()
x = input()
y = input()
x = x.lower()
if x in str:
    compute (str,x,y)
else:
    print('Not Found')