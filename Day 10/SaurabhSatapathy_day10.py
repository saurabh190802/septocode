# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:53:09 2021

@author: saurabh satapathy
"""


def check_string(s):                  #defining the function check                                          
    c=0    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char in s:
            c=c+1
    if c == 26:
        print("Pass")
    if c < 26:
        print("Fail")
        
        
n = int(input())
for i in range(0,n):                #taking input of number of students
    s=str(input())                  #taking input of  string s
    check_string(s)                 #calling check function
                                    
    