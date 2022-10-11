#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5. Escriba un programa que genere una lista con 200 números aleatorios entre 1 y 20,
y luego elimine los elementos que se encuentren repetidos. Debe modificar la lista
existente (no generar una nueva).
"""

import random

lista = []

# Generar los numeros aleatorios
for i in range(0,200):
    randito = random.randint(1,20) # Generar numeros entre el 1 y 20
    lista.append( randito )

# Recorrer la lista
posicion = 0
tamano = len(lista)

while posicion < tamano :
    elemento = lista[posicion]
    
    repeticiones = lista.count(elemento)
    if repeticiones > 1:
        print("El elemento ", elemento," se repite ", repeticiones, " veces ")
        
        while lista.count(elemento) != 1:
            lista.remove(elemento)
            
    posicion = posicion + 1
    tamano = len(lista)

print("===>>>>  Finalizando ....")
for i in range(0,len(lista) ):     
    elemento = lista[i]  
    repeticiones = lista.count(elemento)
    print("El elemento ", elemento," se repite ", repeticiones, " veces ")
