# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 13:27:07 2018
@author: james
"""

import random

#generate random no between 0,1=============================================
x=random.random()
print(x)
#generate random int no.=========================================
x=random.randint(1,10)
print(x)
#Sample randon sample fron iterable object=======================
x=[1,2,3,4,5,6,7,8,9,10]
x=random.sample(x,3)#pick 3 random sample
print(x)
#generate  float no between any two no===============================
x=random.uniform(10,100)
print(x)
#select n bits and return respected decimal no.===========================
x=random.getrandbits(4)
print(x)
#generate random no between two no. including range.
x=random.randrange(1, 10)
print(x)
#choose single element randomly from iterable object============
x=[1,2,3,4,5,6,7,8,9,10]
x=random.choice(x)
print(x)

#Beta distribution. Conditions on the parameters are alpha > 0 and beta > 0. Returned values range between 0 and 1.
x=random.betavariate(1,5)
print(x)

#'choices' k size list with relpacement==========================
x=[1,2,3,5,6,8,99]
x=random.choices(x,k=2)
print(x)

#'expovariate',- expovariate gives you random floating point numbers, exponentially distributed. In a Poisson process the size of the interval between consecutive events is exponential.
x=random.expovariate(15)


#gauss - Gaussian distribution. mu is the mean, and sigma is the standard deviation. This is slightly faster than the normalvariate()
x=random.gauss(1,15)
print(x) 


#getstate -  Return an object capturing the current internal state of the generator. This object can be passed to setstate() to restore the state.
x=random.getstate()
print(x)


# 'setstate',
#setstate()=Python Random setstate() Method in python is used to restore the state to the specified state of the random number generator.
x=random.setstate(x)
print(x)


#normalvariate- normalvariate(mu, sigma) Normal distribution. mu is the mean, and sigma is the standard deviation.
x=random.normalvariate(1,5)
print(x)


#seed  - A random seed specifies the start point when a computer generates a random number sequence. This can be any number, but it usually comes from seconds on a computer system’s clock 
x=random.seed(2)
print(x)

 
#Shuffle - Shuffle a list (reorganize the order of the list items)=======
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)


#triangular(left, mode, right, )===================
#Draw samples from the triangular distribution over the interval 
#[left, right].

#The triangular distribution is a continuous probability 
#distribution with lower limit left, peak at mode,
#and upper limit right. Unlike the other distributions, 
#these parameters directly define the shape of the pdf.
x=random.triangular(2,3,50)
print(x)


#vonmisesvariate(mu, kappa) -mu is the mean angle, expressed in radians between 0 and 2*pi, and kappa is the concentration parameter, which must be greater than or equal to zero. If kappa is equal to zero, this distribution reduces to a uniform random angle over the range 0 to 2*pi.
x=random.vonmisesvariate(1,5)
print(x)


#random.weibullvariate(alpha , beta) -  where alpha is the scale and beta the shape .
y=random.weibullvariate(0,5)#
print(y)

