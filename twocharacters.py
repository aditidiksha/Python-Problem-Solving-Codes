# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:56:28 2020

@author: Hp

"""
from collections import Counter

n=int(input())
l=list(input())

c=Counter(l)
for i,j in c.items():
    if(j==1):
        l.remove(i)
for i in l:
    if(i==(i+1)):
        l.remove(i)
        l.remove(i+1)
