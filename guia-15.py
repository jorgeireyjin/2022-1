#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
15. Implemente un programa que permita introducir dos valores A y B y realice el cálculo de la
expresión S. Muestre el resultado en pantalla.
•
•
Si A >= B
S = 10 + 14 + 18 + … + 50
Si (A / B) <= 30
S = A ^ 2 + B ^ 2
"""

a = int( input("Ingresar el valor de A "))
b = int( input("Ingresar el valor de B "))

if a >= b:
    suma = 0
    inicio = 10
    while inicio <= 50:
        print( inicio , end =" ")
        suma = suma + inicio
        inicio = inicio + 4
    
    print("A >= B, la suma (con while) es " , suma)
        
    # Con FOR
    suma = 0
    x = 10
    for i in range(10,51):
        print( x , end =" ")
        suma = suma + x
        x = x + 4
        if x > 50:
            break
       
    
    print("A >= B, la suma (con for) es " , suma)
    
if  a/b <= 30:
    suma = a**2 + b**2
    
    print("A/B <= 30, la suma es " , suma)    
    