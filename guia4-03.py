#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3. Escriba un programa que lea 10 números enteros y luego los muestre en orden
inverso al que fueron ingresados.
"""

lista = []
i = 0

while i < 10:
    num = int( input("Ingrese un numero ... ") )
    i = i + 1
    lista.append( num )

# Mostrar la lista de numeros
print ( lista )

# Forma 1: Imprimir en orden inverso
i = len(lista) -1
while i >= 0:
    print( lista[i], end=" " )
    i = i - 1

# Forma 2: Imprimir en orden inverso
lista.reverse()
print(lista) 
