#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hacer un programa que genere una lista aleatoria 
(de números entre 0 y 10)  de 5 elementos sin repetición
"""

import random

lista = []

cont = 0

while cont < 5:
    randito = random.randint(0,10)
    
    if randito not in lista:
        lista.append(randito)
        cont = cont + 1
        
print( lista )


