#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:32:05 2022

@author: jin
"""

# Implemente un programa que permita calcular e imprimir la suma: 1+2+3+4+5+…+50

suma = 0
for i in range(1,51):
    suma = suma + i
    
print(suma)

# esto se puede hacer de manera secuencial tambien .... ver Suma de Gauss


#Implemente un programa que permita calcular e imprimir la suma siguiente:
#S = 1 + 4 + 7 + 10 + … + 52

n = 1
suma = 0
while n <= 52:
    suma = suma + n
    n = n + 3
    
print(suma)