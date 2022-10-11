#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Escriba una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelva False. Verifique mayúsculas y minúsculas.
"""

def esVocal( letra ):
    # Usaremos una lista
    vocales = [ 'A', 'E', 'I', 'O','U']

    encontro = False # esta variable sera True si encontramos la vocal
    for i in range(0, len(vocales) ):
        if vocales[i] == letra.upper():
            encontro = True
            break
        
    # Fin del For
    return encontro

# PROGRAMA PRINCIPAL

print( "A es vocal ? ", esVocal("A") )
print( "B es vocal ? ", esVocal("b") )
print( "e es vocal ? ", esVocal("e") )

    
