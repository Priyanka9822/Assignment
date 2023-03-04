amu=int(input("Enter th amount=\t"))
sum1=sum2=sum3=sum4=sum5=sum6=0
while amu>0:
    if amu>=1000:
        N1=amu//1000
        sum1=sum1+N1
        amu=amu-N1*1000
    if amu>=100:
        N2=amu//100
        sum2=sum2+N2
        amu=amu-N2*100 
    if amu>=50:
        N3=amu//50
        sum3=sum3+N3
        amu=amu-N3*50 
    if amu>=20:
        N4=amu//20
        sum4=sum4+N4
        amu=amu-N4*20 
    if amu>=10:
        N5=amu//10
        sum5=sum5+N5
        amu=amu-N5*10 
    if amu>=5:
        N6=amu//5
        sum6=sum6+N6
        amu=amu-N6*5 

print("Total Note",sum1+sum2+sum3+sum4+sum5+sum6)
