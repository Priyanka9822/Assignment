User_id="PythoNCLASS"
Password="Python@3.8"
print('User_id= PythoNCLASS')
print("Password= Python@3.8")

n=input('Enter yor user id:')
if(User_id==n):
    p=input('Enter yor user password:')
    if(Password==p):
        c=1245
        captch=int("E")
        print("Your login successfully")
    else:
        print('Please Enter your correct Password')
else:
    print('Please Enter your correct id')