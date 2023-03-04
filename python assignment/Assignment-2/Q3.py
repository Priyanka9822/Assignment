User_id="PythoNCLASS"
Password="Python@3.8"
c=1245
print('User_id= PythoNCLASS')
print("Password= Python@3.8")
print("c=1245")

n=input('Enter yor user id:')
if(User_id==n):
    p=input('Enter yor user password:')
    if(Password==p):
        captch=int(input("Enter your captch="))
        if(c==captch):
            print("Your login successfully")
        else:
            print("Re-enter your captch")
    else:
        print('Please Enter your correct Password')
else:
    print('Please Enter your correct id')