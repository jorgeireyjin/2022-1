#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
18. Implemente un programa que lea desde el teclado una cadena de caracteres, un valor “n”
que representa el orden de una matriz y permita mostrar el siguiente patrón en pantalla (se
muestran resultados para n = 3 → matriz de 3 x 3).
Si n = 3
palabra = "hola"
hola hola hola
hola hola hola
hola hola hola
"""

n = int( input("Ingresar el valor de N ... ") )
cadena = input("Ingresar una cadena ...")

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print( cadena, end=" " )
    print("")