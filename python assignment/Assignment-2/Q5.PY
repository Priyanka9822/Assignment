print('''
    1.Female
    2.Male
''')
ch=int(input("Enter your Chiose:"))
if(ch==1):
    age=int(input("Enter your Age:"))
    if(age>=18):
        print("Eligibal to Marry")
    else:
        print("Not Eligibal to marry")
if(ch==2):
    age=int(input("Enter your Age:"))
    if(age>=21):
        print("Eligibal to Marry")
    else:
        print("Not Eligibal to marry")
