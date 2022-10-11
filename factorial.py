#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:44:22 2022

@author: jin
"""

def factorial(n):
  rpta = 1
  for i in range(2,n+1):
    rpta = rpta*i
    
  return rpta

# PRograma principal
a = int(input("Ingresar A "))

rpta = factorial(a)
print("La rpta es ", rpta)