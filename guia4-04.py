#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4. Escriba un programa que genere 100 números aleatorios, calcule el promedio y
luego cuente cuántos de estos números están por encima del promedio y cuantos
están por debajo del promedio.
"""

import random

lista = []
suma = 0

# Generar los numeros aleatorios
for i in range(0,100):
    randito = random.randint(0,9) # Generar numeros entre el 0 y 9
    lista.append( randito )
    # Acumular
    suma = suma + randito
    
promedio = suma / 100
porEncima = 0
porDebajo = 0

for i in range(0, len(lista) ):
    if lista[i] > promedio:
        porEncima = porEncima + 1
    else:
        porDebajo = porDebajo + 1
        
print("El promedio es ", promedio)
print("Por encima del Promedio " , porEncima)
print("Por debajo del Promedio ", porDebajo)

    