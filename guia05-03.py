#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3. Escriba una función sum() y una función multip() que sumen y multipliquen respectivamente
todos los números que el usuario ingrese hasta que se digite cero. Luego de leer dicho valor,
mustre en pantalla el resultado final.
"""

def sum():
    suma = 0
    for i in range(0, len(numeros) ):
        suma = suma + numeros[i]
        
    return suma
    
def multip():
    mult = 1
    for i in range(0, len(numeros) ):
        mult = mult * numeros[i]
        
    return mult
    
# PROGRAMA PRINCIPAL

numeros = [] # es una variable Global usada en las funciones
while True:
    num = input("Ingresa un numero - CERO para terminar : ")
    num = int( num )

    if num == 0:
        break
    else:
        numeros.append( num )
    
# Fin del while
suma =  sum()  # Invocar a funcion sum   
multiplicacion = multip() # Invocar a funcion multip
 
# Imprimir resultados
print("La suma es " , suma)
print("la multiplicacion es " , multiplicacion)
    