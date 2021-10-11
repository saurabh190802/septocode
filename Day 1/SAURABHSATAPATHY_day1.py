# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:25:23 2021

@author: saura
"""
def result(a,b,c): #declaring the result function
    ans=int(a+b*c/a-b)
    print(ans)


n=int(input()) #taking input of number of player

for i in range (0,n):
    st = list (map(int, input().strip().split()))[:3]

    a=st[0]
    b=st[1]
    c=st[2]
    result(a, b, c) #calling the result function