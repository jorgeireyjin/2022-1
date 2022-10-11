#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Escriba un programa que tome una lista de números y devuelva la suma
acumulada, es decir, una nueva lista donde el primer elemento es el mismo, el
segundo elemento es la suma del primero con el segundo, el tercer elemento es la
suma del resultado anterior con el tercer elemento y así sucesivamente. Por
ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].
"""

lista = [1,2,3,4,5,6]
rpta = []

rpta.append( lista[0] )

# Recorrer la lista original
for i in range(1, len(lista) ):
    suma = rpta[ i-1 ] + lista[i]
    rpta.append(suma)
    
print(lista)
print(rpta)