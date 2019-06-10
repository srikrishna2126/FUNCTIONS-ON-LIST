# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 00:11:28 2019

@author: HAI
"""

k=[1,2,3,4,'as',':']
print(k[0])
print(k[5])
print(k[4])
k[5]=100
print(k)
k.append(200)
print(k)
k.append('er')
print(k)
k.extend('er')
print(k)
k.pop(5)
print(k)
k.remove(200)
print(k)
k.insert(2,'s')
print(k)
print(k.reverse())
print(k)
print(k.count(4))
kk=[121,13,143,15,1611,17,18]
kk.sort()
print(kk)