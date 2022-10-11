#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hacer una que muestre todos los números perfectos entre 10 y 10000
Para ello debe tener una función que determine si un nḿero es perfecto: 
    eso sucede cuando la sumatoria de los divisores propios del número es igual al mismo número. 
Dicho de otra forma, un número perfecto es aquel que es amigo de sí mismo. 

"""

def esPerfecto( n ):
    suma = 0
    
    for i in range( 1, n):
        if n%i == 0:
            suma = suma + i
    
    if suma == n:
        return True
    else:
        return False
    

def obtenerPerfectos():
    rpta = []
    for i in range(10, 10000):
        if esPerfecto( i ) == True:
            rpta.append( i )
            
    return rpta
    
    
# Programa principal
rpta = obtenerPerfectos()
print( rpta )