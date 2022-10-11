#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hacer un programa que genere una lista aleatoria de 10 elementos y los pase a una función que remueva 
los dos elementos mayores y los dos elementos menores 
(Si un elemento se repite más de dos veces, sólo remover 2 veces)
La función debe retornar la lista con los elementos removidos.
"""
import random

def remover( lista):
    lista.sort()
    print("Lista Ordenada " , lista)
    # Retirar los ultimos  2
    lista.pop()
    lista.pop()
    
    # Retirar los primeros 2
    lista.pop(0)
    lista.pop(0)
    
    return lista
    
# Programa principal
numeros = []

for i in range(0,10):
    randito = random.randint(10,20)
    numeros.append( randito )
    
print("Lista original " , numeros)
nueva_lista = remover( numeros )
print("Nueva lista " , nueva_lista)