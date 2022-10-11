#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:47:57 2022

@author: jin
"""

# Hagamos un juego ....
# ADivina el numero que estoy pensando

num = 5

rpta = int( input("Adivina el numero que tengo ") )

while rpta != num:
    print("No has adivinado, intenta de nuevo")
    rpta = int( input("Adivina el numero que tengo ") )

print(" A D I V I N A S T E ! ! ! !")    