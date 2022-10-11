#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Escribir un programa que tenga una función que calcula la mediana de 3 números aleatorios entre 1 y 100. 
Hay dos posibles algoritmos:
La mediana es el valor que ocupa el lugar central de todos los datos cuando éstos están ordenados de menor a mayor.
O tambien es el resultado de la suma de los valores menos el valor menor menos el valor mayor
"""
import random

def mediana2(a , b, c):
    if ( a < b and b < c) or ( a > b and b> c):
        return b
    
    if ( b < a and a < c) or ( b > a and a> c):
        return a
    
    if ( c < a and b < c) or ( c>a and b > c):
        return c
    
  
    
def mediana1( a, b, c):    
    suma = a + b + c
    return  suma - min(a,b,c) - max(a,b,c)
    
def mediana3(a , b, c):
    lista = [ a , b, c ]
    print( "Lista original " , lista)
    lista.sort()
    print( "Lista Ordenada " , lista)
    
    return lista[1]
    
    
# Programa principal
n1 = random.randint(1,100)
n2 = random.randint(1,100)
n3 = random.randint(1,100)

print("Los alaeatorios son ", n1, " ", n2, " ", n3)
rpta1 = mediana1(n1, n2, n3)
print("La mediana 1 es " , rpta1)

print("La mediana 2 es " , mediana2(n1, n2, n3))

print("La mediana 3 es " , mediana3(n1, n2, n3))
'''
numeros = []
for i in range(0,3):
    randito = random.randint(1,100)
    numeros.append( randito )
'''