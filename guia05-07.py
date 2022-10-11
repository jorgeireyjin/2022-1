#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7. Escriba una función con la siguiente definición:
 imprimirMatriz(n)
Lo que hará esta función será imprimir una matriz cuadrada de dimensiones n x n. Considere
que cada elemento de la matriz será el carácter asterisco (*).
"""


def  imprimirMatriz(n):
    for i in range(0, n):
        for j in range(0, n):
            print( "*", end=" ")
        print("")
    
    
# PROGRAMA PRINCIPAL
n = int( input("Ingresar tamaño de la matriz : "))

imprimirMatriz(n)