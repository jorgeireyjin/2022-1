#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:11:57 2022

@author: jin
"""

# Hacer un progrma que solicite un numero entero de 3 digitos
# Debe mostrar cada digito en una linea separada

num = int( input("Ingrese un numero de 3 digitos ... "))

if num < 100 or num > 999:
    print("Ese no es un numero de 3 digitos")
    
while num != 0:
    digito = num % 10
    num = int(num / 10 )

    print("Digito " , digito)
    #print("Numero " , num)

'''
# Obtener las Decenas
digito = num % 10
num = int(num / 10 )

print("Digito " , digito)
print("Numero " , num)

# Obtener las Centenas
digito = num % 10
num = int(num / 10 )

print("Digito " , digito)
print("Numero " , num)
'''