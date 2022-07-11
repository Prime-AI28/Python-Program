s = input()
x = input()
y = input()

x = x.lower()
y = y.lower()

len_s = len(s)
len_x = len(x)
len_y = len(y)

l = s.split( )
if x in l:
    n = l.index(x)
    l[n] = y
    print(len_s)
    print(len_x)
    print(len_y)
    print (s.index(x))
    for i in l:
        print(i, end = ' ')
