#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 09:51:45 2022

@author: jin

     y = f(x)
     f(x,y,z)
     
"""

import random
import time

def mostrarIntroduccion():
    print('Estás en el tercer ciclo de Ingenieria de Sistemas en la sección 316.') 
    print('Frente a ti hay dos puertas. En una de ellas, la suerte te sonrie y ', end = " " )
    print('te ofrece una oportunidad. En la otra puerta deberás ', end = " ")
    print('enfrentar tu destino engrosando la lista de DESAPROBADOS')
    print()

def elegirPuerta():
    puerta = ''
    while puerta != '1' and puerta != '2':
        puerta = input( '¿Qué puerta deseas abrir ? (1 ó 2)' )

    return puerta

def abrirPuerta(puertaElegida):
    print('Te paras frente a la puerta ...')
    time.sleep(2)
    print('Empiezas a tener frio ...')
    time.sleep(2)
    print('Suena la musica de suspenso ...')
    print()
    time.sleep(2)

    puertaAlAzar = random.randint(1, 2)
    puertaAlAzar = str( puertaAlAzar )

    if puertaElegida == puertaAlAzar :
        texto = '¡SUERTE !!! El destino te brinda una oportunidad'
    else:
        texto = ' OH, que pena ... estas en riesgo de perder el curso'
        
    return texto

# P R O G R A M A   P R I N C I P A L
deseoProbarSuerte = 'si'
while deseoProbarSuerte == 'si' or deseoProbarSuerte == 's':
    mostrarIntroduccion()
    puerta = elegirPuerta()
    rpta = abrirPuerta(puerta)
    
    print("... y el resultado es ... " , rpta)

    print('¿Quieres probar de nuevo? (escribe si o no)')
    deseoProbarSuerte = input().lower()
    
print("Fin")