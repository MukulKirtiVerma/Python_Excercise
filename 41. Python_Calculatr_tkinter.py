# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:49:19 2019

@author: james
"""



import math
import tkinter as tk
root = tk.Tk()
exp=tk.StringVar()

root.configure(background='gray')
root.geometry("220x300")
def cal(x):
   
    if(x=="="):
       exp.set(eval(exp.get()))
    else:
        exp.set(exp.get()+x)
def clear_b():
    exp.set("")
def s_clear():
    exp.set(exp.get()[:len(exp.get())-1])    
    
def math_sqrt():
    exp.set(str(math.sqrt(int(eval(str(exp.get()))))))
def math_squire():
    exp.set(str(int(eval(exp.get()))**2))
    
        


w = tk.Label(root, textvariable=exp, height=5, background="white", width=30)
w.grid(column=0,row=0,columnspan=4,padx=2,pady=2)




b1=tk.Button(text="<--",height=2,width=5 , command=lambda : s_clear())
b1.grid(column=0,row=1,padx=1,pady=2)

b2=tk.Button(text="C",height=2,width=5, command=lambda : clear_b())
b2.grid(column=1,row=1,padx=1,pady=2)

b3=tk.Button(text="sqrt",height=2,width=5, command=lambda : math_sqrt())
b3.grid(column=2,row=1,padx=1,pady=2)

b4=tk.Button(text="Sqr",height=2,width=5, command=lambda : math_squire())
b4.grid(column=3,row=1,padx=1,pady=2)

b5=tk.Button(text="1",height=2,width=5, command=lambda : cal('1'))
b5.grid(column=0,row=2,padx=1,pady=2)

b6=tk.Button(text="2",height=2,width=5, command=lambda : cal('2'))
b6.grid(column=1,row=2,padx=1,pady=2)

b7=tk.Button(text="3",height=2,width=5, command=lambda : cal('3'))
b7.grid(column=2,row=2,padx=1,pady=2)

b8=tk.Button(text="+",height=2,width=5, command=lambda : cal('+'))
b8.grid(column=3,row=2,padx=1,pady=2)

b9=tk.Button(text="4",height=2,width=5, command=lambda : cal('4'))
b9.grid(column=0,row=3,padx=1,pady=2)

b10=tk.Button(text="5",height=2,width=5, command=lambda : cal('5'))
b10.grid(column=1,row=3,padx=1,pady=2)

b11=tk.Button(text="6",height=2,width=5, command=lambda : cal('6'))
b11.grid(column=2,row=3,padx=1,pady=2)

b12=tk.Button(text="-",height=2,width=5, command=lambda : cal('-'))
b12.grid(column=3,row=3,padx=1,pady=2 )

b13=tk.Button(text="7",height=2,width=5, command=lambda : cal('7'))
b13.grid(column=0,row=4,padx=1,pady=2)

b14=tk.Button(text="8",height=2,width=5, command=lambda : cal('8'))
b14.grid(column=1,row=4,padx=1,pady=2)

b15=tk.Button(text="9",height=2,width=5, command=lambda : cal('9'))
b15.grid(column=2,row=4,padx=1,pady=2)

b16=tk.Button(text="*",height=2,width=5 , command=lambda : cal('*'))
b16.grid(column=3,row=4,padx=1,pady=2)

b17=tk.Button(text="0",height=2,width=5, command=lambda : cal("00"))
b17.grid(column=0,row=5,padx=1,pady=2)

b18=tk.Button(text=".",height=2,width=5, command=lambda : cal("."))
b18.grid(column=1,row=5,padx=1,pady=2)

b19=tk.Button(text="=",height=2,width=5, command=lambda : cal('='))
b19.grid(column=2,row=5,padx=1,pady=2)
b20=tk.Button(text="/",height=2,width=5, command=lambda : cal('='))
b20.grid(column=3,row=5,padx=1,pady=2)


root.mainloop()

