#Remove Enter Key from Dictionary

e={1000:"KAPUR",1002:"SWAMI",1003:"SWAPNIL",1004:"ASHVINI",1005:"Balaji"}
print(e)
key=int(input("Enter A KEY TO Remove:"))
if key in e:
    e.pop(key)
    print(e)
else:print("key not present")

