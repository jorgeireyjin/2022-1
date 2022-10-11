#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
12. Los pedidos de una tienda se encuentran representados utilizando 2 listas: P y C. La
primera contiene el precio unitario en soles de cada uno de los productos y la segunda la
cantidad de unidades que se solicitó. Implemente una función en Python que reciba ambas
listas, muestre el subtotal por cada producto y retorne el monto total del pedido. Considere
que los precios tienen incluido el impuesto.
Ejemplo:
P = [2.55, 8, 10.5]
C = [3, 2, 2]

Tendremos entonces, por ejemplo, que se adquirieron 3 unidades Producto 1 a 2.55 soles
cada una.
El subtotal se obtendrá multiplicando los valores correspondientes en las listas P y C.
La función mostrará:
Subtotal producto 1: 5.1 soles
Subtotal producto 2: 16 soles
Subtotal producto 3: 21 soles
Adicionalmente, la función retornará 42.1.

"""
def totaliza( p, c ):
    total = 0
    for i in range(0, len(p)):
        subtotal = p[i]*c[i]
        print("Subtotal producto " , i , " = " , subtotal)
        #print("Subtotal producto %2d = %5.2f" % (i, subtotal) )
        total = total + subtotal
        
    return total
        

# PROGRAMA PRINCIPAL
P = [2.55, 8, 10.5]
C = [3, 2, 2]

print("El total es : ", totaliza(P,C) )