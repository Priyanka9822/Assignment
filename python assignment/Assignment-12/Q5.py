#Sum All items in dictionary

dic={1:1,2:4,3:9,4:16,5:25}
sum=0

for k,v in dic.items():
    sum+=v+k
print("Sum of Values:\t",sum)