#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
14. Implemente un programa que determine el conjunto de números que hay entre la unidad y
un determinado número introducido por el teclado. Tomando en cuenta el grupo de
números mencionado, su programa debe imprimir, sumar y contar los números del grupo
que son a la vez múltiplos de 2 y de 3.
"""

# INtriduciendo un numero por teclado
num = int( input("Ingresar un numero") )

suma = 0 # acumulador
cont = 0 # contador
# determine el conjunto de números que hay entre la unidad y un determinado número introducido por el teclado.
for i in range(1,num + 1):
    # san la vez múltiplos de 2 y de 3
    if i % 2 == 0 and i%3 == 0:
        print(i, end=" ")
        suma = suma + i
        cont = cont + 1

print( " " )
print(" Fin ")