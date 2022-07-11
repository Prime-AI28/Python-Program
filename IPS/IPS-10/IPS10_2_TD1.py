N = int(input())

p=set()
m=set()
s=set()

crt = set(range(51,101))

for i in range(0,N):
    phy = int(input())
    p.add(phy)

for i in range(0,N):
    mat = int(input())
    m.add(mat)

for i in range(0,N):
    sci = int(input())
    s.add(sci)

p_p = len(p.intersection(crt))
p_f = len(p.difference(crt))

m_p = len(m.intersection(crt))
m_f = len(m.difference(crt))

s_p = len(s.intersection(crt))
s_f = len(s.difference(crt))

print("No. of Pass in Physics", p_p)
print("No. of Failure in Physics",p_f)

print("No. of Pass in Maths", m_p)
print("No. of Failure in Maths", m_f)

print("No. of Pass in Science", s_p)
print("No. of Failure in Science", s_f)