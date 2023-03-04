cost_price=float(input("enter the COST PRICE:"))
diss=float(input(" Enter the Disscount  :"))
diss=diss/100
dp=cost_price*diss
sp=cost_price-dp
print("DISSCOUNT PRICE:",dp,"\n","Selling Price:",sp)