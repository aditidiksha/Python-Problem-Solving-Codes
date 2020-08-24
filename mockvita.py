# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 03:41:37 2020

@author: Hp
"""

n=int(input())
l=list(map(int,input().split()))
l1=[]
c,c1,c2 = 0,0,0
for i in range(0,len(l)):
    largest = 0
    smallest = 9
  
    while (l[i]): 
        r = l[i] % 10
        largest = max(r, largest) 
  
        # Find the smallest digit 
        smallest = min(r, smallest) 
  
        l[i]= l[i] // 10
    lar=largest*11
    sma=smallest*7
    sum=lar+sma
    sum1=str(sum)
    if(len(sum1)<=2):
        l1.append(sum1)
    else:
        l1.append(sum1[1:])
print(l1)
for i in range(0,10):
    for j in range(0,n,2):
        if(l1[j][0]==str(i)):
            c+=1
    if(c<=1):
        c1+=0
    elif(c==2):
        c1+=1
    elif(c>2):
        c1+=2
    c = 0
for i in range(0,10):
    for k in range(1,n,2):
        if(l1[k][0]==str(i)):
            c+=1
    if(c<=1):
        c2+=0
    elif(c==2):
        c2+=1
    elif(c>2):
        c2+=2
    c=0
print(c1+c2)
            
        
    