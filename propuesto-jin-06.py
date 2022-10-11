#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6. Escriba un programa que permita el ingreso de un numero “n” entero positivo menor que 20 y luego genere la figura siguiente. 
Considerar que “n” es el tamaño de la matriz a generar.
"""


n = int( input("Ingrese un numero menor a 20 :"))
for i in range(0,n):
    for j in range(0, n-i):
        print(" ", end=" ")
    
    for k in range(0,i):
        print("*",end=" ")
    print("")