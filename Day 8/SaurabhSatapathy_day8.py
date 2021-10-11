# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:12:58 2021

@author: saurabh satapathy
"""
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    if d["UPPER_CASE"]>d["LOWER_CASE"]:
        print(s.upper())
    if d["UPPER_CASE"]<d["LOWER_CASE"]:
        print(s.lower())
    if d["UPPER_CASE"]==d["LOWER_CASE"]:
        print(s.lower())

t = int(input())
for i in range(0,t):
    s=str(input())
    string_test(s)


