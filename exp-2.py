#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LISTAS
"""

lista = []  # Lista vacia
lista2 = [ 'a','e','i','o','u',1,2,3]

print(" Tamaño de la lista " , len(lista2))
print(" Elemento en posicion 0 " , lista2[7])

for i in range(0, len(lista2) ):
    print("Posicion " , i, "Elemento " , lista2[i])
    
# Agregar elementos
lista.append("Python")
lista.append("Java")
print( lista )
lista.append("C++")
print(lista)

lista.insert(1,"Cobol")
print(lista)


a = [1,2,3]
b = [ 4,5,6]
a.append(b)
print ( a )

