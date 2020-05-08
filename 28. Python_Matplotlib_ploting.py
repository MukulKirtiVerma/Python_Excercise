# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 16:51:03 2018

@author: Mukul Kirti Verma
"""


"""
1. sipmle chart
2. bar chart
3. histogram
4. box
5. area 
6. scatterd
7. pie chart
"""

#run line one byy one or conert it to notebook for better visualization


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#plot seriese
x=pd.Series(data=[1,2,3,2])
#x=[0,1,2,3]
x.plot()
plt.plot(x,)


#graph attribute
"""
figsize
facecolor
dpi
"""

#figure size change graph size

from matplotlib.pyplot import figure
plt.figure(figsize=(8, 6), dpi=80, facecolor='b')
plt.plot(x)

#change marker
from matplotlib.pyplot import figure
#dash line marker
plt.plot(x,'--')
#change color with dash line
plt.plot(x,'r--')
#add some point in line
plt.plot(x,'r--o')


""" Some marker
Markers
character	description
'-'	solid line style
'--'dashed line style
'-.'dash-dot line style
':'	dotted line style
'.'	point marker
','	pixel marker
'o'	circle marker
'v'	triangle_down marker
'^'	triangle_up marker
'<'	triangle_left marker
'>'	triangle_right marker
'1'	tri_down marker
'2'	tri_up marker
'3'	tri_left marker
'4'	tri_right marker
's'	square marker
'p'	pentagon marker
'*'	star marker
'h'	hexagon1 marker
'H'	hexagon2 marker
'+'	plus marker
'x'	x marker
'D'	diamond marker
'd'	thin_diamond marker
'|'	vline marker
'_'	hline marker
"""


"""
The following color abbreviations are supported:

character	color
'b'	        blue
'g'	        green
'r'	        red
'c'	        cyan
'm'	        magenta
'y'	        yellow
'k'	        black
'w'	        white
"""


""" some other attribute
linewidth
axis
legend
"""
#a.plot(x1, y1, 'g^', x2, y2, 'g-')


plt.plot([1,2,3], [1,2,3], 'go-',  linewidth=5)
plt.plot([1,2,3], [1,4,9], 'rs',  )
plt.axis([0, 4, 0, 10])



"""Some other attribute
xlim
ylim
legend()
"""


plt.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
plt.plot([1,2,3], [1,4,9], 'rs',  label='line 2')
plt.legend()
plt.xlim(0,5)
plt.ylim(0,9)


#some othe attrib
"""
linestyle
marker
markersize
markerfacecolor
"""
plt.plot(x,x, color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)


"""
change background color"""
plt.rcParams['axes.facecolor'] = 'black'
plt.plot(x)



import numpy as np
import matplotlib.pyplot as plt

print(plt.style.available)

with plt.style.context(('dark_background')):
     plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
plt.show()



"""Some other attrib
fontsize
titlesize
labelsize
xlabel
ylabel
"""
import matplotlib.pyplot as plt

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure titlepl
plt.subplot(111, xlabel='x', ylabel='y', title='title')
plt.plot(x)



#Note that you can also set the sizes calling the rc method on matplotlib:
    
    
    
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

matplotlib=plt
matplotlib.rc('font', **font)
matplotlib.rcParams.update({'font.size': 22})



import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})

"""
xlabel
ylabel
title
"""
import matplotlib.pyplot as plt
plt.subplot(111, xlabel='x', ylabel='y', title='title')
plt.plot(x)


import matplotlib

SMALL_SIZE = 8
matplotlib.rc('font', size=SMALL_SIZE)
matplotlib.rc('axes', titlesize=SMALL_SIZE)



csfont = {'fontname':'Comic Sans MS'}
hfont = {'fontname':'Helvetica'}

plt.title('title',**csfont)
plt.xlabel('xlabel', **hfont)
plt.plot(x)



#Multiplot

plt.plot(x, x, 'g^', x*2, x*2, 'g-')




#Specifying the order of matplotlib layers
import matplotlib.pyplot as plt

lineWidth = 20
plt.figure()
plt.plot([0,0],[-1,1], lw=lineWidth, c='b',zorder=1)
plt.plot([-1,1],[-1,1], lw=lineWidth, c='r',zorder=2)
plt.plot([-1,1],[1,-1], lw=lineWidth, c='g',zorder=3)
plt.show()



#simple chart

#1======================
l=[]
for i in range(1,30):
    l.append(i**4)
ts1=pd.Series([x**4 for x in range(1,30)])
ts1.plot()


#=======================
ts2=pd.Series([x*x*x for x in range(1,30)])
ts2.plot()


#2=====================
ts3=pd.Series([x*x for x in range(1,30)])
ts3.plot()



#3 multiple line=======

df=pd.DataFrame()
df.insert(0, "ts1", ts1)
df.insert(1, "ts2", ts2)
df.insert(2, "ts3", ts3)
plt.figure(); 
df.plot();

#======================
plt.figure();
df.plot(color=['red','green','blue'] );


#==========================
df = pd.DataFrame(data=np.random.randn(1000, 4), columns=list('ABCD'))
df = df.cumsum()
df.plot();


#========================
plt.figure(); 
df.plot(subplots=True);
plt.figure()

      
#========================
#bar chart       
#1      

df.iloc[5].plot(kind='bar');
df.plot(kind='bar');


#2 multiple bar chart=========
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot.bar();


#stacked bar chart===========
df2.plot.bar(stacked=True);
#stacked horizontal bar chart======
df2.plot.barh(stacked=True);

#hishtogram====================
df4 = pd.DataFrame({'a': np.random.randn(1000) , 'b': np.random.randn(1000),'c': np.random.randn(1000)}, columns=['a', 'b', 'c'])

#set opecity===================
plt.figure();
df4['a'].hist()
df4['a'].hist(grid=False)
df4.hist()


#===============================
#change color===================
df4 = pd.DataFrame({'a': np.random.randn(1000) , 'b': np.random.randn(1000),'c': np.random.randn(1000)}, columns=['a', 'b', 'c'])
plt.figure();
df4['a'].hist()
df4['b'].hist(color='blue')
df4['c'].hist(color='red')
df4.hist()

#==============================
df4.hist(grid=False)


#==============================
df4.plot.hist()


#=================================
df4.plot.hist(alpha=0.3,grid=True)
df4.plot.hist( alpha=0.3)


#==================================
#horizontal histogram

df4.plot.hist(orientation='horizontal')



#box plots=======================
df = pd.DataFrame(np.random.rand(10), columns=['A'])
df['A'].plot.box()

#==============Multiple box chart===========
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df['A'].plot.box()
df['B'].plot.box()
df['C'].plot.box()
df.plot.box( positions=[1, 4, 5, 6, 8])

#=====================================
df.plot.box()


#change color=======================
color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians='DarkBlue', caps='Gray')
df.plot.box(color=color)


#vertical box plot==================
df.plot.box(vert=False)
df.plot.box(vert=False, positions=[1, 4, 5, 6, 8])
df.plot.box()


#example2============================
df = pd.DataFrame(np.random.rand(10,5))
plt.figure();
df.boxplot(grid=True)

#grouping==============================
df = pd.DataFrame(np.random.rand(10,2), columns=['Col1', 'Col2'] )
df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B'])
plt.figure()
bp = df.boxplot(by='X',).color('red')
df.groupby(by='X')
df.plot.box(color=color)


#area chart===========================
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area();

#==============change color=========
df.plot.area(color=['green','red']);


#Scaterd chart=====================
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c','d'])
df.plot.scatter(x='a', y='b');
plt.scatter(df['a'],df['b'],color='Yellow')

#============================================
plt.scatter(df['c'],df['d'],color='DarkGreen')
plt.show()

#==================make group=============
axi = df.plot.scatter(x='a', y='b', color='Yellow', label='Group 1');

df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=axi);



#Pie chart=================================
series = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')

series.plot.pie(figsize=(5, 5))



#compair two pi chart======================
df = pd.DataFrame(np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y'])
df.plot.pie(subplots=True, figsize=(8, 4))

#=====================================    
series = pd.Series([.4] * 4, index=['a', 'b','c','d'], name='series2')
series.plot.pie(figsize=(6, 6))

#======================================
df=pd.DataFrame([0.2] * 5, index=['a', 'b', 'c', 'd',e])
df.plot.pie(figsize=(6, 6),)

