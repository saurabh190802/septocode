# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 10:06:26 2021

@author: saurabh satapathy
"""

def  abs_diff(a,n):                        #defining abs_diff function
    row_sum=0
    col_sum=0
    for i in range(0,n):
        row_sum = row_sum+a[0][i]+a[n-1][i]
        col_sum = col_sum+a[i][0]+a[i][n-1]
    print(abs(row_sum - col_sum))



t = int(input())      # taking input of number of test cases


for i in range(t):
    a=[]
    n = int(input())  #taking input of no of rows and column for square matrix
    for k in range(0,n):    
        a.append([int(j) for j in input().split()])  
    abs_diff(a,n)       #calling abs_diff function