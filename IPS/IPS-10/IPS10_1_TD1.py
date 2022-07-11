labrec = {}
for i in range (0,3):

    Test = input()
    MinVal_Test = int(input())
    MaxVal_Test = int(input())

    labrec[Test] = (MinVal_Test,MaxVal_Test)

p_test = input()
p_val = int(input())

min = labrec[p_test][0]
max = labrec[p_test][1]

if min<= p_val<=max:
    print("Normal")
else:
    print("Abnormal")


    
