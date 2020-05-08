# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 18:38:31 2018

@author: james
"""
#!pip install tkinter


from tkinter import *
import tkinter as Tk
root=Tk()
root.mainloop()

from tkinter import *
root=Tk()
b1 = Button(root,text="welcome" )
b1.pack()
root.mainloop()


activebackground
activeforeground
anchor
bg
fg
cursor
bitmap

from tkinter import *
root=Tk() 
b1 = Button(root,text="welcome" ,activebackground="green",activeforeground="yellow",height=10, width=50)
b1.pack()
root.mainloop()

from tkinter import *
root=Tk()
b1 = Button(root,text="welcome" ,background="red",fg="lightgreen",anchor="s",height=32, width=32)
b1.pack()
root.mainloop()

from tkinter import *
root=Tk('500X500')
root.title("asd")
mm=PhotoImage(file=r"b1.gif")
b1 = Button(root,text="welcome", cursor="Mouse", image=mm,relief=FLAT)
b1.pack()
root.mainloop()


import tkinter


#compound

from tkinter import *
root=Tk()
mm=PhotoImage(file=r"d:\tut\b1.gif")
b1 = Button(root,text="welcome",compound="center",height=550,anchor="s",width=700, cursor="Mouse", image=mm,)
b1.pack()
b1.flash()
root.mainloop()


#command


from tkinter import *
master = Tk()
def callback():
    print("click!")
b = Button(master, text="OK", command=callback,default=DISABLED)
b.pack()
mainloop()


#relief  RAISED/SUNKEN/

from tkinter import *
master = Tk()

b = Button(master, text="OK", relief=FLAT)
b.pack()
mainloop()


from tkinter import *
root=Tk("800X800")
mm=PhotoImage(file=r"d:\tut\b1.gif")
b1 = Button(root,text="welcome",compound="center",anchor="s",cursor="Mouse",relief="flat" ,image=mm,)
b1.pack()
root.mainloop()

RAISED

from tkinter import *
master=Tk()
b=Button(master,text="welcome" , relief=RAISED)

b.pack()
master.mainloop()




default

from tkinter import *
master=Tk()
b=Button(master,text="welcome" , default=DISABLED)
b.pack()
master.mainloop()


font

from tkinter import *
master=Tk()
b=Button(master,text="welcome",font="Verdana 20 bold" )
b.pack()
master.mainloop()


"""
justify
overrelief
The colors 
 'white'
 'black'
 'red'
 'green'
 'blue'
 'cyan'
 'yellow'
 'magenta' """

from tkinter import *
master=Tk()
textt="""my name is 
mukul"""
b=Button(master,text=textt,justify="left")
b.pack()
master.mainloop()



from tkinter import *
master=Tk()
textt="""my name is 
mukul"""
b=Button(master,text=textt,highlightcolor="white",justify="center")
b.pack()
master.mainloop()


from tkinter import *
root=Tk()
mm=PhotoImage(file=r"d:\tut\b11.gif")
b1 = Button(root,text="welcome",compound="center",height="50",anchor="s", width=200, cursor="Mouse", image=mm,)
b1.pack()
root.mainloop()

overrelief
/
from tkinter import *
master=Tk()
textt="""my name is 
mukul"""

b=Button(master,text=textt,overrelief=FLAT)
b.pack()      
master.mainloop()


padx
pady
repeatdelay	#after button press it will wait
repeatinterval	#when repetedelay called repet interval press in this time interwal
"""
from tkinter import *
master=Tk()
textt="""my name is 
mukul""""""

from tkinter import *
master = Tk()
def callback():
    print("click!")
    print("ok")
b = Button(master, padx=20,pady=30,text="OK", command=callback,repeatdelay	=5000,repeatinterval=3000)
b.pack()   
master.mainloop()


from tkinter import *
master = Tk()
def callback():
    print("click!")
    print("ok")
b = Button(master, padx=20,pady=30,text="OK", command=callback,repeatdelay	=5000)
b.pack()   
master.mainloop()

from tkinter import *
master = Tk()
def callback():
    print("click!")
    print("ok")
b = Button(master, padx=20,pady=30,text="OK", command=callback,repeatinterval=3000)
b.pack()   
master.mainloop()


state	
Disabeled/Normal

from tkinter import *
master = Tk()
def callback():
    print("click!")
b = Button(master, text="OK", state=DISABLED , command=callback)
b.pack()   
master.mainloop()

from tkinter import *
master = Tk()
def callback():
    print("click!")
b = Button(master, text="OK", state=NORMAL)
b.pack()   
master.mainloop()


takefocus# tab will not work
highlightthickness #to set size of control in squair shape

from tkinter import *
master = Tk()
def callback():
    print("click!")
b = Button(master, text="OK", takefocus="off"  ,highlightthickness=50)
b.pack()   
master.mainloop()



.get()
.set(value)
textvariable


from tkinter import *
master = Tk()
var2=StringVar()
var2.set("hi")
def fun():
    var2.set("hello")
    print(var2.get())

#    b.update()
b = Button(master, textvariable=var2, command=fun)

b.pack()   
#b.update()
print(var2.get())
master.mainloop()



underline
from tkinter import *
master = Tk()
b = Button(master, text="OK hello", underline=3)
b.pack()   
master.mainloop()



wraplength
i
c
m
from tkinter import *
master = Tk()
b = Button(master, text="OK hello tfygjhkghj", underline=3,wraplength="1i")
b.pack()   
master.mainloop()




canvas
create line
from tkinter import *
master = Tk()
canvas_width = 80
canvas_height = 40
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack(fill=BOTH)
y = int(canvas_height / 2)
w.create_line(0, 0, 80, 40, fill="#476042")
mainloop()


from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()
w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()


master = Tk()
w = Canvas(master, width=200, height=100)
w.pack()
w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
w.create_rectangle(50, 25, 150, 75, fill="blue")
i = w.create_line(xy, fill="red")
w.coords(i, new_xy) # change coordinates
w.itemconfig(i, fill="blue") # change color
w.delete(i) # remove
w.delete(ALL)
mainloop()


line box
from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_rectangle(50, 20, 150, 80, fill="#476042")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0, 0, 50, 20, fill="#476042", width=3)
w.create_line(0, 100, 50, 80, fill="#476042", width=3)
w.create_line(150,20, 200, 0, fill="#476042", width=3)
w.create_line(150, 80, 200, 100, fill="#476042", width=3)

mainloop()



ovel
C.create_oval ( x0, y0, x1, y1, option, ... )
from tkinter import *
canvas_width = 190
canvas_height =150
master = Tk()
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()
w.create_oval(60,60,100,80)
mainloop()



Painting Interactively into a Canvas
from tkinter import *
canvas_width = 500
canvas_height = 150
def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x  ), ( event.y )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = "red" )
master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
mainloop()


Drawing Polygons
create_polygon(x0,y0, x1,y1, x2,y2, ...) 
from tkinter import *

canvas_width = 200
canvas_height =200
python_green = "#476042"

master = Tk()

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

points = [0,0,canvas_width,canvas_height/2, 0, canvas_height]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)

mainloop()



The Canvas Image Item

from tkinter import *
master = Tk()
w = Canvas(master)
w.pack()
img=PhotoImage(file=r"d:\tut\python_logo.gif")
w.create_image(20,20, image=img)
mainloop()








