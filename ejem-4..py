#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:04:20 2022

@author: jin
"""

# Iteraciones anidadas : tabla de multiplicar

for i in range(1,13):
    for j in range(1,13):
        print( "%3d" % (i*j) , end = " ")
    # aqui termina j
    print(" ")
# aqui termina i