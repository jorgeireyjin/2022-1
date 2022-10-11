#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:47:57 2022

@author: jin
"""

# Hagamos un juego ....
# ADivina el numero que estoy pensando

num = 5

while True :
    print("No has adivinado, intenta de nuevo")
    rpta = int( input("Adivina el numero que tengo ") )
    
    if rpta == num:
        break

print(" A D I V I N A S T E ! ! ! !")    