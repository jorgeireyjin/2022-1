#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
17. Implemente un programa que permita imprimir en pantalla el siguiente patrón tomando
como entrada un valor “n” que determina la cantidad de líneas que se imprimirán (el
ejemplo muestra lo que debe mostrarse para para n = 3 → 3 líneas):
****
********
************
"""

n = int( input("Ingresar un numero N "))

patron = "****"
cadena = patron
for i in range(1,n + 1):
    print(cadena)
    cadena = cadena + patron