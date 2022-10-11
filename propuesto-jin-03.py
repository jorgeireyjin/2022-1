#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3. Implemente un programa que permita ingresar dos números enteros positivo y luego muestre el Máximo común divisor (MCD).
NOTA: Debe utilizar funciones
"""

def mcd(a,b):
    divisores_a = divisores( a )
    divisores_b = divisores( b )
    comunes = []
    
    # Hallar los factores comunes de a en b
    for i in range(0, len(divisores_a)):
        elemento = divisores_a[i]
        # Buscar el elemento en los divisores de B
        for j in range(0, len(divisores_b)):
            if divisores_b[j] == elemento:
                comunes.append( elemento )
                break
    
    print( comunes )
    return comunes[-1]
    

def divisores( n ):
    rpta = []
    for i in range(1, n ):
        if n%i == 0:
            rpta.append(i)
            
    return rpta
    

# PROGRAMA PRINCIPAL
a = int ( input("Ingrese un numero A : "))
b = int ( input("Ingrese un numero B : "))

print("El MCD es  ", mcd(a,b) )