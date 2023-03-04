#Given key exist in Dictionary or NOT

student={1:"sham",2:"ram",3:"priya",4:"pornima",5:"karma"}
key=int(input("Enter A key:"))
for k in student.keys():
    if k==key:
        print("Key is present")
        break
else:
        print("Key is NOT present")
        