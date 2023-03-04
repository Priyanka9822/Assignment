'''Accept the basic salary of n employ(n should be accept from user)
if basic salary below 20,000 then da=10%,ta=12%,hra=15% otherwise da=15%
ta=18% and hra=20%.Based on this calculate thesalary of each employ
and also salary of All employ'''




noOfEmploy=int(input("Enter the no employ in company="))
sum=0
for i in range(1,noOfEmploy+1):
    Name=input("Enter Employ Name=")
    Bsal=int(input("Enter Basic Salary="))
    if(Bsal<=20000):
        ta=Bsal*0.12
        da=Bsal*0.10
        hra=Bsal*0.15
        Tsal=Bsal+ta+da+hra
        print("Salary of",Name,'is=',Tsal)
    else:
        ta=Bsal*0.18
        da=Bsal*0.15
        hra=Bsal*0.20
        Tsal=Bsal+ta+da+hra
        print("Salary of",Name,'is=',Tsal)
    sum=sum+Tsal
print("ALL Employ salary is=",sum)