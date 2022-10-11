#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Defina una función max() que tome como argumentos dos números y devuelva el mayor de
ellos. Luego genere una nueva función que pueda recibir 3 números en vez de dos.
"""

def max1( a , b ):
    mayor = 0
    if a > b :
        mayor = a
    elif b > a:
        mayor = b
    else:
        mayor = a
        
    return mayor

def max2( a , b ):
    mayor = -9999
    if a > mayor :
        mayor = a
        
    if b > mayor:
        mayor = b
        
    return mayor

def max3(a , b , c ):
    # Que psa si comparo de 2 en 2
    mayor = max1(a, b )
    rpta =  max1( mayor, c)
    return rpta
    
    
# PROGRAMA PRINCIPAL
print( max1(15,10) )
print( max2(10,15) )
print( max3(10,15,30) )
print( max3(30,15,10) )
print( max3(15,30,10) )