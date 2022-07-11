name =  input()
marks = []
for i in range (0,4):
    m = int(input())
    if (m>-1 and m<101):
        marks.append(m)
    else:
        print("Invalid Input")
        quit()
s = sum(marks)

result = []

for j in marks:
    if (j < 50) :
        result.append('fail')
    elif (j>= 50 and j<60):
        result.append('e')
    elif (j>=60 and j<70):
        result.append('d')
    elif (j>=70 and j<80):
        result.append('c')
    elif (j>=80 and j<90):
        result.append('b')
    elif (j>=90 and j<95):
        result.append('a')
    elif (j>=95 and j<100):
        result.append('s')
result.append(s)
avg = s/4
result.append(avg)

l = marks + result

rec = {name: l}

print(rec)