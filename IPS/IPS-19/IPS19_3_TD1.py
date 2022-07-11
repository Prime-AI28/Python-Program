BP = int(input())
DA = int(input())
HRA = int(input())
Loan = int(input())
LIC = int(input())

gross = BP + DA + HRA
deduction = Loan + LIC
Net = gross - deduction

fo = open('Salary.txt','w')
fo.write(str(BP)+'\n'+str(DA)+'\n'+str(HRA)+'\n'+str(Loan)+'\n'+str(LIC)+'\n'+str(gross)+'\n'+str(deduction)+'\n'+str(Net))
fo.close()

fo = open('Salary.txt','r')
print(fo.read())
fo.close()
