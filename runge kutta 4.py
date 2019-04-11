# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:49:31 2019

@author: gagan


python implementation of runge kutta 4 th order 

"""

x0 = eval(input("enter the initial value of xo:"))
y0 = eval(input("enter the initial value of yo:"))
xn = eval(input("enter the final limit:"))
h = eval(input("enter the interval:"))
x = x0
y = y0

def f(x,y):
    m = x + y
    return m

while(x < xn):
    m1 = f(x0, y0)
    m2 = f((x0 + h/2.0), (y0 + m1*h/2.0))
    m3 = f((x0 + h/2.0), (y0 + m2*h/2.0))
    m4 = f((x0 + h), (y0 + m3*h))
    m = (m1 + 2*m2 + 2*m3 + m4)/6
    y = y + m*h
    x = x + h
    
    print(x,"\t\t\t\t",y)
