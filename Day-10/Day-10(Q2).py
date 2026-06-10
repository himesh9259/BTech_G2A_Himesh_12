i=1
n=int(input("enter number of rowes"))
while n>0:
    space =1
    while space <=i:
        print(" ",end='')
        space+=1
    j=1
    while j<=(n*2)-1:
        print("*",end='')
        j+=1
    print()
    n=n-1
    i+=1
        
