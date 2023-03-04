n=int(input(" Enter the Amount to get required Note:"))
SUM=0

N1=n//1000
n1=n%1000
print("1000 NOTE NO= ",N1)
    
N2=n1//100
n2=n1%100
print("100 NOTE NO= ",N2)
   
N3=n2//50
n3=n2%50
print("50 NOTE NO ",N3)
        
N4=n3//20
n4=n3%20
print("20 NOTE NO= ",N4)
    

N5=n4//10
n5=n4%10
print("10 NOTE NO= ",N5)
    
N6=n5//5
n6=n5%5
print("5 COIN NO= ",N6)
    
N7=n6//2
n7=n6%2
print("2 COIN NO= ",N7)
    
N8=n7//1
n8=n7%1
print("1 COIN NO= ",N8)
sum=N1+N2+N3+N4+N5+N6+N7+N8
print(" TOTAL NOTE =",sum)