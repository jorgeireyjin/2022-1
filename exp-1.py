#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 18:43:28 2022

@author: jin
"""

inicio = 1
final = 10

for x in range( inicio, final ):
    print( x , end =" " )
    
print(" ")
# con while
while inicio < final:
    print ( inicio , end =" ")
    inicio = inicio + 1
    
