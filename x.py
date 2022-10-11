#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:36:19 2022

@author: jin
"""

def funcionSinArgumento() :
    print("NO tengo argumento")
    
def funcionConArgumento(x):
    print("El argumento es ", x)

def funcionCon2Argumentos(x, y):
    print("El argumento es ", x, y)
    
def funcionSinArgumento2() :
    print("NO tengo argumento")
    return 'XYZ'
    
# Programa principal
funcionSinArgumento()

funcionConArgumento(999)

funcionCon2Argumentos(1,"X")

rpta = funcionSinArgumento2()
print("La funcion retorna " , rpta)