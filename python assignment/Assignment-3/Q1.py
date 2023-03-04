

Userid="Swami"
Password="Swami@9822"
captch="5423"
print("Userid=Swami")
s=(input("Enter the user id:"))
if(Userid==s):
    print("Enter your password=Swami@9822")
    for i in range(1,4):
        p=(input("Enter pass:")) 
        if Password==p:
            captch="5423"
            print("Enter your captch=",captch)
            c=int(input("captch:"))
            if(c==captch):
                print("You are login succssfully")

            else:
                print("Enter correct captch")
                captch+=1
        else:
            if(i==1):
                print("Enter correct password only 2 chance remaining")
            if(i==2):
                print("Enter correct password only 1 chance remaining")
        
else:
    print("Enter correct user id")

'''if(Userid==s):
    print("Enter your password=Swami@9822")
    for i in range(1,4):
        p=(input("Enter pass:")) 
    if Password==p:
        captch="5423"
        print("Enter your captch=",captch)
        c=int(input("captch:"))
        if(c==captch):
            print("You are login succssfully")
        else:
            print("Enter correct captch")
            captch+=1
    else:
        if(i==1):
            print("Enter correct password only 2 chance remaining")
        if(i==2):
            print("Enter correct password only 1 chance remaining")
        
else:
    print("Enter correct user id")'''
