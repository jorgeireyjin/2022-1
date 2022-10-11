#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6. Escriba un programa en Python que, dada una lista de nombres y una letra,
devuelva una lista con todos los nombres que empiezan por dicha letra.
"""

nombres = ['Pedrito','Luchito','Pepito','Carlita']
letra = input("Ingrese una letra ...")

letra = letra.upper()


for i in range(0, len(nombres)):
    elemento = nombres[i]
    
    if letra == elemento[0]:
        print( elemento )
