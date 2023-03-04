sa=int(input("Enter the no of student in class:"))
asp=0
st=sa
i=1
while sa>0:
    s1=int(input("Enter the ENG mark="))
    s2=int(input("Enter the MARATHI mark="))
    s3=int(input("Enter the HINDI mark="))
    s4=int(input("Enter the MATH mark="))
    s5=int(input("Enter the SCIENSE mark="))

    SUM=s1+s2+s3+s4+s5
    per=(SUM*100//500)
    print("percentage of student",i,"is=",per,"%")
    asp=asp+per
    sa-=1
    i+=1
print("Average of all student is=",asp//st,"%")