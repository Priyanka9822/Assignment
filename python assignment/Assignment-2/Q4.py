sub1=float(input("Enter your Mark SUB 1:\t"))
sub2=float(input("Enter your Mark SUB 2:\t"))
sub3=float(input("Enter your Mark SUB 3:\t"))
sub4=float(input("Enter your Mark SUB 4:\t"))
sub5=float(input("Enter your Mark SUB 5:\t"))
sum=sub1+sub2+sub3+sub4+sub5
per=(sum/500)*100
if(per>=75):
    print("First Class")
elif(per>=65):
    print("Second Class")
elif(per>=55):
    print("Third Class")
else:
    print("Pass")