# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 23:58:37 2019

@author: james
"""

t=input()
t=int(t)
s1=0
s2=0

while(t):
    t-=1
    a=[]
    n=int(input())
    k=int(input())
    if(n<2 or k<2):
        print(0)
        continue
    if(k%n==0):
        s1=0
        s2=0
    else:
        for i in range(k%n):
            a.append((k//n)+1)
        for j in range(n-(k%n)):
            a.append(k//n)
        a.sort()
        a.reverse()
        b=[]
        i=0
        j=len(a)-1
        if((k%n)>(n-k%n)):
            while(i<=j):
                b.append(a[i])
                if(i!=j):
                    b.append(a[j])
                i=i+1
                j=j-1
        else:
            while(i<=j):
                b.append(a[j])
                if(i!=j):
                    b.append(a[i])
                i=i+1
                j=j-1
        #print(b)
        i=1
        s2=0
        
        while(i<len(b)):
            xx=(b[i]-b[i-1])
            if(xx<0):
                xx=xx*-1
            s2=s2+xx
            i+=1+1-1
    print(s2)
        