s = input()

c_a = 0
c_e = 0
c_i = 0
c_o = 0
c_u = 0

for i in s:
    if i == 'a':
        c_a += 1
    elif i == 'e':
        c_e += 1
    elif i == 'i':
        c_i += 1
    elif i == 'o':
        c_o += 1
    elif i == 'u':
        c_u += 1

if (c_a >0):
    print("a is",c_a)
if (c_e > 0):
    print("e is",c_e)
if (c_i > 0):
    print("i is",c_i)

if (c_o > 0):
    print("o is",c_o)
    
if (c_u > 0):
    print("u is",c_u)

if (c_a == 0 and c_e == 0 and c_i == 0 and c_o == 0 and c_u == 0):
    print("None")