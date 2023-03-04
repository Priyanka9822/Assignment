tp=int(input(" Total no persons:\t"))
t=int(input(" full ticket:\t"))
sum1=sum2=sum3=tct=tst=tpt=0
while tp>0:
    age=int(input(" Enter age:\t"))
    tp-=1
    if age>59:
        tst=t*0.50
        sum1=sum1+tst 

    if age<12:
        tct=t*0.30
        sum2=sum2+tct
        
    if 12<=age<=59:
        tpt=t
        sum3=sum3+tpt
        
print("child ticket=",sum2)
print("senior Ticket=",sum1)
print("person Ticket=",sum3)
print("Total Amount",sum1+sum2+sum3)