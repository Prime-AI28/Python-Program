n = int(input())
m = int(input())
z = int(input())
if n>0 and m>0 and z>0:
    def compute(n,m,z):
        x = lambda a,b,c: (a*b*c)/100
        print(int(x(n,m,z)))
else:
    def compute():
        print ("Invalid Input")
compute(n,m,z)