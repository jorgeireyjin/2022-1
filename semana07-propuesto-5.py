#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    5. Haga un programa que ingrese un número entero positivo “n”. 
    Luego tomando las letras del abecedario, genere “n” palabras de “n” caracteres 
    aleatorios
Ejemplo: si ingreso 4 como número, el programa debe generar
“akue” , “pwqn” , “dfrg” ,”xyzn”

Usar Funciones

"""
import random

def generarPalabras(n):
    rpta = []
    for i in range(0, n):
        palabra = formarPalabra(n)
        rpta.append( palabra)
    
    return rpta
    
def formarPalabra(n):
    abc = "abcdefghijklmnopqrstuvwxyz"
    palabra = ""
    # Obtener n caracteres en base a numeros aleatorios
    for i in range(0,n):
        randito = random.randint(0, len(abc)-1 )
        letra = abc[randito]
        palabra = palabra + letra        
        
    return palabra

# Progrma principal
n = int( input("Ingrese un numero : "))

if n <= 0:
    print("este programa no funcionara ...")
else:
    print("Rsultado es ", generarPalabras(n))