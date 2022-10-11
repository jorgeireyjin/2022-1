#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7. Desarrolle el programa "eliminar_duplicados" que reciba una lista y devuelva una
nueva lista con los elementos únicos (que no estén repetidos) de la lista original.
"""

import random

lista = []

# Generar los numeros aleatorios
for i in range(0,200):
    randito = random.randint(1,20) # Generar numeros entre el 1 y 20
    lista.append( randito )
    
# Ver la lista generada
print(lista)    
rpta = []

# Recorrer la lista inicial
for i in range(0,200):
    elemento = lista[i]
    
    try:
        if rpta.index(elemento) != 0:
            pass
    except:
        rpta.append(elemento)
        
print(rpta)