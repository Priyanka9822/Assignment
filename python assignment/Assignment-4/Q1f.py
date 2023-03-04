for h in range( 1, 6):
    for k in range (1,h+1):
        if h==3 and k==2 or h==4 and k==2 or h==4 and k==3:
            print(" ",end="  ")
        else:
            print(k,end="  ")
    print()