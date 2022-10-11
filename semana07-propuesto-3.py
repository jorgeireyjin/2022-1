#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    3. Implemente un programa que permita ingresar dos números enteros 
    positivo y luego muestre el Máximo común divisor (MCD).
NOTA: Debe utilizar funciones

"""
def mcd(a , b ):
    divisores_a = divisores( a )
    divisores_b = divisores( b )
    
    comunes = []
    # Hallar los numeros comunes de la lista a en la lista b
    for i in range(0, len(divisores_a) ):
        elemento = divisores_a[i]
        
        # Buscar elemento en la lista de divisores_b

        for j in range(0, len(divisores_b)):
            if  divisores_b[j]  == elemento:
                comunes.append( elemento )
                break
            
    print(divisores_a)
    print(divisores_b)
    print(comunes)
    
    return comunes[-1] # return comunes[ len(comunes) - 1]
           
                
    
def divisores(n) :
    rpta = []
    for i in range(1, n+1):
        if  n % i == 0:
            #print(i, end=" ")
            rpta.append( i )
    return rpta

# PROGRAA PRINCIPAL
a = int( input("Ingrese un numero A : ") )
b = int( input("Ingrese un numero B : ") )

rpta =  mcd( a , b )
print("El MCD de ", a, " y " , b , " es " , rpta)