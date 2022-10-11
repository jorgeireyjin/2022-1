#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
8. Desarrolle el programa “hacer_compras”, el cual imprimirá una lista de instrucciones
de compra para un empleado. Tome en cuenta las siguientes reglas:
a. Deberá empezar con la instrucción “Ir a la tienda”, incluso para una lista
vacía.
b. Para cada artículo de nuestra lista deberá imprimir “Comprar <nombre
artículo>”
c. Al finalizar la lectura deberá colocar el mensaje “Pagar por los <n>
artículos”
Ejemplo: >>> hacer_compras([‘papas’,’leche’])
Ir a la tienda
Comprar papas
Comprar leche
Pagar por los 2 artículos
"""

print("Ir a la tienda")

lista = [ 'Pan', 'Leche','Jamon','Queso']

# Cantidad de articulos a comprar
cont = 0

while cont < len(lista):
    print("Comprar ", lista[cont])
    cont = cont + 1

print("pagar por los ", cont," articulos")