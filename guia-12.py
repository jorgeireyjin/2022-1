#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:40:42 2022

@author: jin
"""

'''
12. Implemente un programa que permita introducir dos números por teclado e imprimir los
números que hay entre ellos comenzando por el más pequeño. Muestre cuántos números
son, cuántos de ellos son pares y la suma de valores pares que hay en el grupo mencionado.
'''

num1 = int(input("Ingrese un numero "))
num2 = int(input("Ingrese otro numero "))

mayor = 0
menor = 0

# Determinar quien es el mayor
if num1 > num2:
    mayor = num1
    menor = num2
elif num2 > num1:
    mayor = num2
    menor = num1
else:
    mayor = num1
    menor = num2
    
cont = 0 # contar cuanto numeros son
pares = 0 # contar cuantos son pares
suma = 0 # suma de valores pares    
for i in range(menor, mayor+1):
    cont = cont + 1
    if i % 2  == 0:
        pares = pares + 1
        suma = suma + i
        
print("Cuantos numeros son " , cont )
print("Cuantos pares hay " , pares)
print("La suma de pares es ", suma)
    