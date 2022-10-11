#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:54:33 2022

@author: jin
"""


# Imprimir los 10 primeros nuneros pares

cont = 0
for i in range(1,31):
            
    if i % 2 == 0:
        print( i )
        cont = cont + 1
        
    if cont == 10:
        continue
        
print("Se imprimio ", cont)