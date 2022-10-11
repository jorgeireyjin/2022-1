#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9. Implemente una función en Python que reciba como entrada un número de segundos inferior
a un millón y calcule su equivalente considerando días, horas, minutos y segundos. Tome en
cuenta que:
1 minuto = 60 segundos.
1 hora = 60 minutos = 3600 segundos.
1 día = 24 horas = 1440 minutos = 86400 segundos
"""

def equivalente( segundos ):
    SEG_X_MIN = 60
    SEG_X_HORA = 3600
    SEG_X_DIA = 86400

    print("El equivalente es:")
    
    cant_dias = segundos // SEG_X_DIA
    print(cant_dias, "dia(s)")
    segundos = segundos % SEG_X_DIA

    cant_horas = segundos // SEG_X_HORA
    print(cant_horas, "hora(s)")
    segundos = segundos % SEG_X_HORA

    cant_minutos = segundos // SEG_X_MIN
    print(cant_minutos, "minuto(s)") 
    segundos = segundos % SEG_X_MIN
    
    print(segundos, "segundos(s)")

segundos = int( input("Ingrese la cantidad de segundos :"))
equivalente(segundos)

