s = input()
find = input()
count = 0
sl = s.lower()

for i in sl:
    if find == i:
        count +=  1
print(count)

for j in range (len(s)-1,-1,-1):
    print(s[j], end= '')