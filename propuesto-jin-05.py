#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5. Haga un programa que ingrese un número entero positivo “n”. 
Luego tomando las letras del abecedario, genere “n” palabras de “n” caracteres aleatorios
Ejemplo: si ingreso 4 como número, el programa debe generar
“akue” , “pwqn” , “dfrg” ,”xyzn”

"""
import random

def formaPalabra(n):
    abc = "abcdefghijklmnopqrstuvwxyz"
    palabra = ""
    # Obtener n numeros aleatorios
    for i in range(0,n):
        num = random.randint(0, len(abc)-1 )
        palabra = palabra + abc[num]
    
    return palabra
        
def generarPalabras(n):
    rpta = []
    for i in range(0, n):
        palabra = formaPalabra(n)
        rpta.append(palabra)
    
    return rpta
    
n = int (input("Ingrese un numero : "))

print("Resultado es " , generarPalabras(n) )
