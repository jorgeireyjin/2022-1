#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:36:30 2022

@author: jin
"""

# Implemente un programa que permita introducir un número entero positivo a través del
#teclado y e imprima en pantalla un mensaje indicando si es par o impar. El programa
#deberá continuar leyendo hasta que le usuario ingrese un valor -1.

#-- una manera de resolver

while True:
    num = int( input("Ingresa un numero ... "))
    
    if num % 2 == 0:
        print("el numero es PAR")
    else:
        print("El numero es IMPAR")
        
    if num == -1:
        break

print("Fin")