#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    2. Implemente un programa que permita introducir un número entero positivo a 
    través del teclado y luego imprima en pantalla todos sus divisores en una 
    sola línea. El programa deberá continuar leyendo hasta que le usuario 
    ingrese un valor -1.
NOTA: Ahora utilice funciones.
Por ejemplo , si el usuario ingresa 10
El programa debe imprimir  1 2 5 10

VARIACION 1: Debe retornar una lista de divisores
VARIACION 2 : Debe retornar una cadena con la rpta
"""
def divisores(n) :
    rpta = "" # Cadena vacia
    for i in range(1, n+1):
        if  n % i == 0:
            #print(i, end=" ")
            rpta = rpta + "-" + str(i)
    return rpta

# PROGRAMA PRINCIPAL

print("Usando funciones")
#El programa deberá continuar leyendo hasta que le usuario 
# ingrese un valor -1.
while True:
    n = int( input("Ingrese un numero N : ") )
    
    if n == -1:
        break
    
    if n > 0:
        # Los divisores
        rpta = divisores(n)
        print( rpta )
        
    
print("Fin")
