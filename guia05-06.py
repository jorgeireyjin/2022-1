#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6. Escriba un programa que tenga una función que retorne factorial de un número ingresado
por consola.
"""

def fact(n):
  rpta = 1
  for i in range(2,n+1):
    rpta = rpta*i
    
  return rpta

# PRograma principal
a = int(input("Ingresar A "))

rpta = fact(a)
print("La rpta es ", rpta)