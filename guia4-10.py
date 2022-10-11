#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10. Genere una lista con los nombres de los asistentes a un evento. Luego realice la
búsqueda de un nombre ingresado como parámetro.
Si el nombre ingresado se encuentra en la lista de asistentes, muestre el mensaje
“Estuvo en el evento”, en caso contrario muestre: “No estuvo en el evento”.
"""

nombres = ['Luchito','Sandrita','Carlitos','Adita','Clarita']

nom = input("Ingrese el nombre a buscar ...")
encontro = False

for i in range(0, len(nombres) ):
    
    elemento = nombres[i].upper() # COnvertir a mayuscula
    if elemento == nom.upper():
        encontro = True
        break
    
if encontro:
    print("Estuvo en el evento")
else:
    print("NO estuvo en el evento")