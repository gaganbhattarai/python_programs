# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:13:53 2019

@author: gagan
"""

#chi square test for rolling of dice

import numpy as np
observed = np.array(eval(input("enter the observed frequency of  :")))
for i in range(len(observed)):
    expected  = sum(observed)/len(observed)
    print(expected)
calculate = np.array((observed - expected)**2)/expected
print(calculate)
sum_of_calculate = calculate.sum()

print("the calculated chi square value is :",sum_of_calculate)
alpha_tabulated = 18
    
if sum_of_calculate < alpha_tabulated:
    print(sum_of_calculate,"<",alpha_tabulated)
    print("hence, hypothesis is accepted")
else:
    print(sum_of_calculate, "> ", alpha_tabulated)
    print("hence, hypothesis is rejected")