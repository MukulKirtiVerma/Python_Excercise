# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:45:07 2020

@author: Mukul Kirti Verma
"""

#ptython recursion

#Simple Recursion=====================
def fun( n) :
    if(n==0):#base condition
        return
    print("hello")
    fun(n-1)#recursive call
fun(5)    
  



#5*4*3*2*1   computation through recursion===============
def fum(n):
   if(n==1):
       return 1
   else:
       return n * fum(n-1)
fum(5)    

    
#  python recursive code for fibonaci=======================
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#some example
def fun(n,m):
    
    if(m>5):
        return 0
    else:
        m=m+1
        return n + fun(n*3,m)
fun(5,1)



#another way to fibonaci
def fib(n):
    if n == 0:
        
        return 0
    elif n == 1:
        
        return 1
    else:
        
        return fib(n-2) + fib(n-1)
for i in range(0,8) :   
    print(fib(i))



#===============================================
#Exceed the limit of recursion
import sys
sys.setrecursionlimit(1500)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(500))


#some complex codes===============================
#check out the outputs
def fun(n):
    if(n>=5 ):
        return
    else:
        
        fun(n+1)
        print(n)
        fun(n+2)
        print(n)
        return
fun(1)



#try yourself to convert these c++ recursive code int o python
"""
int fun(int x, int y) 
{
  if (x == 0)
    return y;
  return fun(x - 1,  x + y);
} 





 
void fun(int n)
{
  if (n == 0)
    return;
 
  printf("%d", n%2);
  fun(n/2);
}  





int fun(int x, int y)
{
    if (y == 0)   return 0;
    return (x + fun(x, y-1));
}





int fun(int x, int y)
{
    if (y == 0)   return 0;
    return (x + fun(x, y-1));
}
 
int fun2(int a, int b)
{
    if (b == 0) return 1;
    return fun(a, fun2(a, b-1));
}






#include<stdio.h>
void print(int n)
{
    if (n > 4000)
        return;
    printf("%d ", n);
    print(2*n);
    printf("%d ", n);
}
 
int main()
{
    print(1000);
    getchar();
    return 0;
}





#include<stdio.h>
void print(int n)
{
    if (n > 4000)
        return;
    printf("%d ", n);
    print(2*n);
    printf("%d ", n);
}
 
int main()
{
    print(1000);
    getchar();
    return 0;
}






#include <stdio.h>
int f(int n)
{
    if(n <= 1)
        return 1;
    if(n%2 == 0)
        return f(n/2);
    return f(n/2) + f(n/2+1);
}
 
 
int main()
{
    printf("%d", f(11));
    return 0;
}




#include<stdio.h>
int f(int *a, int n)
{
  if(n <= 0) return 0;
  else if(*a % 2 == 0) return *a + f(a+1, n-1);
  else return *a - f(a+1, n-1);
}
  
int main()
{
  int a[] = {12, 7, 13, 4, 11, 6};
  printf("%d", f(a, 6));
  getchar();
  return 0;
}





#include <stdio.h>
int fun(int n, int *f_p)
{
    int t, f;
    if (n <= 1)
    {
        *f_p = 1;
        return 1;
    }
    t = fun(n- 1,f_p);
    f = t+ * f_p;
    *f_p = t;
    return f;
}
 
int main()
{
    int x = 15;
    printf (" %d n", fun(5, &x));
    return 0;
}





int f(int j)
{
  static int i = 50;
  int k;
  if (i == j)
  {
    printf("something");
    k = f(i);
    return 0;
  }
  else return 0;
}


"""



