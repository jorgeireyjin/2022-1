#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    1. Implemente un programa que permita introducir un número entero 
    positivo a través del teclado y luego imprima en pantalla todos 
    sus divisores en una sola línea. El programa deberá continuar 
    leyendo hasta que el usuario ingrese un valor -1.
NOTA: No utilice funciones.
Por ejemplo , si el usuario ingresa 10
El programa debe imprimir  1 2 5 10
"""

# PROGRAMA PRINCIPAL

while True:
    n = int( input("Ingrese un numero N : ") )
    
    if n == -1:
        break
    
    if n > 0:
        # Los divisores
        cont = 0
        for i in range(1, n+1):
            if  n % i == 0:
                cont = cont + 1
                print(i, end=" ")
        
        if  cont == 2:
            print("El numero es primo")
    
print("Fin")