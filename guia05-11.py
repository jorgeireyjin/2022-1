#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
11. Implemente una función en Python que reciba una lista L y retorne una nueva lista
considerando solamente aquellos elementos que sean mayores que el elemento situado a
su izquierda y que el elemento situado a su derecha.
Ejemplo:
L = [10, 33, 22, 55, 21]
Para estos valores el programa retornará [32, 55].
El valor 32 es mayor que 10 y 22. De igual forma, el valor 55 es mayor que 22 y 21.
"""


def nuevaLista( lista ):
    rpta = []
    
    for i in range( 1, len(lista) - 1):
        print( lista[i-1] , " - " , lista[i] , " - " ,lista[i+1])
        if ( lista[i] > lista[i-1] ) and (lista[i] > lista[i+1] ) :
            print(True)
            rpta.append( lista[i] )
            
    return rpta
    

# PROGRAMA PRINCIPAL
L = [10, 33, 22, 55, 21]

print( L )
print( nuevaLista( L ) )
