# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 08:45:48 2019

@author: gagan
"""

r= [0.11,0.54,0.68,0.73,0.98]
#print(max(r))
n=len(r)
for i in range(len(r)):
                 j=i+1
                 d1 = [((j/n)-r[i])]
                 d2 = [(r[i]-((j-1)/n))]
                 print(d1,"\t\t\t",d2)
                 
dplus = max(d1)
dminus = max(d2)
d =max(dplus,dminus)
dalpha = 0.565
if dalpha > d:
    print("\naccepted")
else:
    print("\nrejected")