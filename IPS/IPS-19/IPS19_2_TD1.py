name = input()
age = input() 
address = input() 
connum = input()
reason = input()

fo = open("patient.txt",'w')
fo.write(name + '  ' + age + '  ' + address + '  ' + connum + '  ' + reason )
fo.close()

fo = open('patient.txt','r')
read = fo.read()
fo.close()

l = read.split("  ")
for i in l:
    print(i)
