for i in range(1,50):
    h=2
    while(h<=i-1):
        if(i%h==0):
            break
        else:
            h+=1
    if h==i:
        sn=i
        print(sn,end=" ")