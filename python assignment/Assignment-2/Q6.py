t=int(input("ENTER THE Ticket:"))
age1=int(input("Enter the Age 1 person :"))
age2=int(input("Enter the Age 2 :"))
age3=int(input("Enter the Age 3 :"))
age4=int(input("Enter the Age 4 :"))
age5=int(input("Enter the Age 5 :"))
tct=0
tcs=0
tpt=0
if(age1,age2,age3,age4,age5<12):
    tc=int(input("Total no child:"))
    tct=t*0.3*tc
    print("Child Ticket:",tct)
if(age1,age2,age3,age4,age5>59):
    ts=int(input("Total no of senior:"))
    tcs=t*0.5*ts
    print("senior Ticket:",tcs)
if(12<=age1,age2,age3,age4,age5<=59):
    tp=int(input("Total no youth:"))
    tpt=t*tp
    print("youth Ticket:",tpt)
sum=tct+tcs+tpt
print("Total Amount:",sum)