import sys
while(1):
    def fun(x):
        status="yes"
        for i in range(len(x)-1):
            if(x[i]>=max(x[i+1:])): pass
            else: status="no"
        return status
            
    x=input("enter 0 to exit")
    if(int(x)==0):
        sys.exit()
    y=input("choose no")
    a=[]
    y=y.split(" ")
    
    for i in y:
    	a.append(int(i))
    aa=a.copy()
    aa.sort()
    for i in aa:
        ix=a.index(i)
        st=fun(a[:ix])
        if(st=="no"):
            print("no")
            break
        else:
            a.pop(ix)
    else:
        print("yes")

