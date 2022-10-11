#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:45:17 2022

@author: jin
"""

lista = [ 'a','b', 'c','x','y','z']
for i in range(0, len(lista) ):
    print( lista[i])
    
# Forma 1
tupla = tuple(lista)
for i in range(0, len(tupla) ):
    print( tupla[i])
    
# Forma 2
for elem in tupla:
    print( elem )


print( tupla[-1] , " -- " , tupla[5] )

# Slicing
print( tupla[2:3] )
print( tupla[2:5] )
print( tupla[2:5:2] )

print ( 'x' in tupla )

if 'x' in tupla:
    print( "Si esta")
else:
    print("No esta")
    
    
print("=====================================")

recta = [ (0,0,0) , (5,8,3) ]

coord1 = recta[0]
coord2 = recta[1]

x, y , z = coord2
print( "x=", x, " y=", y , " z=" , z)

paso1 = recta[1]
paso2 = paso1[0]


print( "x= ", recta[1][0])
print( "y= ", recta[1][1])
print( "z= ",recta[1][2])

















