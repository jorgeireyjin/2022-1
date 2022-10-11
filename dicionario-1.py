#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:45:32 2022

@author: jin
"""

a = { 'Nombre' : 'Superman' , 'Poder' : 'Fuerza', 'Comic' : 'Marvel' }

b = dict( Nombre='Superman' ,Poder='Fuerza',  Comic='Marvel')

print(a)
print(b)

print( a['Poder'])
#print( a['xyz'])

print( "usando get " , a.get('Poder') )
print( "usando get " , a.get('xyz') )

a['Origen'] = 'Kripton'
print(a)

a['Comic'] = 'DC'
print(a)

del a['Origen']
print(a)

a.clear()
print(a)

a = { 'Nombre' : 'Superman' , 'Poder' : 'Fuerza', 'Comic' : 'Marvel' }
lista = a.items()
print(lista)

for e in lista:
    print( e[0] , '- ', e[1])


keys = a.keys()
print(keys)
for k in keys:
    print( k , ' - ' , a[k] ) 

values = a.values()
print(values)


