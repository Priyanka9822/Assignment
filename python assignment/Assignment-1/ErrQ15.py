n=int(input(" Enter the Amount to get required Note:"))
SUM=0
if(n>0):
    N1=n//1000
    n1=n%1000
    print(N1)
    if(n1==0):
        sum=N1
        print("NOTE=",sum)
if(n1>0):
    N2=n1//100
    n2=n1%100
    print(N2)
    if(n2==0):
        sum=N1+N2
        print("NOTE=",sum)
if(n2>0):
    N3=n2//50
    n3=n2%50
    print(N3)
    if(n3==0):
        sum=N1+N2+N3
        print("NOTE=",sum)       
if(n3>0):
    N4=n3//20
    n4=n3%20
    print(N4)
    if(n4==0):
        sum=N1+N2+N3+N4
        print("NOTE=",sum)
        n4=0
if(n4>0):
    N5=n4//10
    n5=n4%10
    if(n5==0):
        sum=N1+N2+N3+N4+N5
        print("NOTE=",sum)
if(n5>0):
    N6=n5//5
    n6=n5%5
    if(n6==0):
        sum=N1+N2+N3+N4+N5+N6
        print("NOTE=",sum)
if(n6>0):
    N7=n6//2
    n7=n6%2
    if(n7==0):
        sum=N1+N2+N3+N4+N5+N6+N7
        print("NOTE=",sum)
if(n7>0):
    N8=n7//1
    n8=n7%1

sum=N1+N2+N3+N4+N5+N6+N7+N8
print("Numbers of NOTE requird=",sum)










