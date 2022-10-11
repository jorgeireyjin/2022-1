#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:40:35 2022

@author: jin
"""

n = int( input("Ingrese un numero menor a 20 :"))
for i in range(0,n):
    for j in range(0, n-i):
        print(" ", end=" ")
    
    for k in range(0,i):
        print("*",end=" ")
    print("")