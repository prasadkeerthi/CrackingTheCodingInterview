# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:21:31 2018

@author: keerthi prasad
"""
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

name="John wick had a dog"
print(name)

for x in name:
    print(x)
    a=name.index(x)
    if(x==' '):
        k=name[:a]+'%20'+ name[a+1:]
        name=k
        
name=k
print(k)
       