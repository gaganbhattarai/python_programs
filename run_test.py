# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 20:15:43 2019

@author: gagan
"""

import numpy as np
import math 
again = True
count = 0
count1 = 0

#data = np.array(eval(input("enter the list elements:  ")))
data = np.array([0.12,0.01,0.23,0.28,0.89,0.3,0.64,0.28,0.33,0.93,0.34])
mean = 0.495

for num in data:
    if(num<mean):
        if(again):
            count = count+1
            again = False
            again1 = True
    else:
        if(again1):
            count1 = count1+1
            again = True
            again1 = False
print("negative",count)
print("positive",count1)
#
b = count + count1
print("the total number of run is:", b)
N = len(data)

greater = [num for num in data if num > mean]
print(greater)
lower = [num for num in data if num < mean]
n1 = len(greater)
n2 = len(lower)


meu_b = ((2*n1*n2/N) + (1/2))
print("the meu value is",meu_b)
sigma_square_b = round(((2*n1*n2*(2*n1*n2 - N))/(N**2*(N-1))), 4)
print("the sigma square b value is:", sigma_square_b)
sigma_b = round(math.sqrt(sigma_square_b), 4)
print("the value of sigma b is:", sigma_b)
cal_Zo = round((b - meu_b)/sigma_b, 4)
print("the value of Zo is:", cal_Zo)

def test_hypothesis(n):
    if n >= -1.96 and n<=1.96:
        print("\naccepted")
        print("the data is uniformly distributed")
    else:
        print("rejected")
test_hypothesis(cal_Zo) 