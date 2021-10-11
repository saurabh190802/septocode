# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:15:22 2021

@author: saurabh satapathy
"""

def step_counts(n):                      #defining step_count function
    step = 0
    while n > 1:
        if n % 2 == 0:
            n = n//2
            step += 1
        elif n % 2 == 1:
                n = n//2
                step += 1
    print(step)
    
t = int(input())                        #taking input of number of test cases
for i in range(t):
    n = int(input())                    #taking input of nummber of marbles
    step_counts(n)                      #calling step_count function

