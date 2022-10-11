#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Implemente un programa que permita introducir un número entero positivo a través del teclado y luego imprima en pantalla todos sus divisores en una sola línea. El programa deberá continuar leyendo hasta que le usuario ingrese un valor -1.
NOTA: No utilice funciones.
Por ejemplo , si el usuario ingresa 10
El programa debe imprimir  1 2 5 10
"""

# PROGRAMA PRINCIPAL
while True:
    n = int(input("ingrese un numero N :"))
    
    if n == -1:
        break

    # Los divisores
    for i in range(1, n+1):
        if n%i == 0:
            print(i, end=" ")
            
            