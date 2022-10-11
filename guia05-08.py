#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
8. Un número es capicúa si se lee igual de izquierda a derecha y de derecha a izquierda. Por
ejemplo: 232 es capicúa, pero 123 no lo es. Desarrolle un programa que imprima un mensaje
diciendo si un número es capicúa o no. Para ello programe dos funciones con las siguientes
definiciones:
• invertir(n)
• es_palindromo(n)

La función es_palindromo recibirá como argumento un número entero n y luego lo enviará
a la función inversa(n), la cual retornará el número invertido. Luego comparará ambos
números, el original y el invertido, e imprimirá un mensaje diciendo si el número cumple o
no con ser capicúa.
"""
def invertir(n):
    cad = str(n)
    nuevo_num = ""
    for i in range(0, len(cad)):
        nuevo_num = cad[i] + nuevo_num

    num = int(nuevo_num)
    return num
    
    
def es_palindromo(n):
    if n == invertir(n):
        print(n ," es palindromo")
    else:
        print(n, "NO ES palindromo")
    
# PROGRAMA PRINCIPAL
  
num = int(input("Ingresar un numero entero positivo : "))
es_palindromo(num)
