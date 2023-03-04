n=int(input("Enter A NUMBER:"))
a=n
srev=0
while(n!=0):
    rev=n%10
    srev=srev*10+rev
    n=n//10
if(a==srev):
    print("Palindrome")
else:
    print("Not Palindrome")