# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:21:31 2018

@author: keerthi prasad

This program takes a string and replaces spaces with %20
"""


name=input("enter the string")
print("the string is",name)

for x in name:
    
    a=name.index(x)
    if(x==' '):
        k=name[:a]+'%20'+ name[a+1:]
        name=k
        
name=k
print("Urlified string is",k)
       