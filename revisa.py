# -*- coding: utf-8 -*-
"""
7. Escriba una función con la siguiente definición:
imprimirMatriz(n)
Lo que hará esta función será imprimir una matriz cuadrada de dimensiones 
n x n. Considere que cada elemento de la matriz será el carácter asterisco (*).
"""


n = 7

def imprimirMatriz(n):
    '''
    for i in range(0, n+1):
        print('*'*i)
    '''
    
    for i in range(0, n+1):
        for e in range(0, i): # Se imprime los astericos en función de las filas
            print('*', end = '')
        print('')

imprimirMatriz(n)
