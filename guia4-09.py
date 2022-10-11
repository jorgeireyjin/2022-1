#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9. Genere dos listas que tengan el mismo tamaño (solicitará el tamaño por teclado).
En una de ellas almacene nombres de personas como cadenas, en la otra lista
debe ir almacenando la longitud de cada nombre.
Luego del ingreso de datos, su programa debe mostrar por pantalla cada nombre y
la longitud que tiene.
"""

tam = int(input(" INgresar el tamaño de las listas "))
nombres = []
tamanos = []

cont = 0
while cont < tam:
    nom = input("Ingrese un nombre ")
    nombres.append(nom)
    tamanos.append( len(nom))
    cont = cont + 1
    
print(nombres)
print(tamanos)

# Mostrar
for i in range(0, len(nombres)):
    print( nombres[i] , " Longitud -> ", tamanos[i])