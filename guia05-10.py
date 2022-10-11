#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10. Implemente una función en Python que reciba una lista de números enteros y un
exponente “n”. Su función deberá modificar cada uno de los elementos de la lista,
elevándolos a la potencia “n”.
"""


def potencia( lista, n):
    for i in range(0, len(lista)):
        elemento = lista[i]
        lista[i] = elemento**n
        
    return lista
    
    
# PROGRAMA PRINCIPAL
lista = [1,2,3,4,5,6,7,8 ]

n = int( input("Ingrese la potencia N : "))

print(lista)
print( potencia(lista, n) )