'''
Un número es divisible entre 11 cuando la suma de los números que ocupan la posición par menos la suma de 
los números que ocupan la posición impar es igual a 0 o a un número múltiplo de 11.
'''
def esMultiplo11(n):
  n = str(n)
  num = list(n)
  # Posiciones pares
  sumaPares = 0
  sumaImpares = 0
  for i in range(0, len(num)):
    if ( i+1 ) % 2 == 0:
      sumaPares = sumaPares + int(num[i])
    else:
      sumaImpares = sumaImpares + int(num[i])

  resta = sumaPares - sumaImpares
  if resta == 0 or resta%11 == 0:
    return True
  else:
    return False


rpta = []   
for i in range(100,500):
  if esMultiplo11(i):
      rpta.append(i)
      
print(rpta )


'''
Dos números naturales distintos son amigos si a cada uno de ellos se lo obtiene sumando los divisores propios 
del otro. 
Los divisores propios de un número incluyen la unidad pero no al propio número.
a b a
Ejemplos: 1) 10 y 8 no son amigos puesto que los divisores propios de 10 son 1,2,5 cuya suma es 8, pero los divisores propios de 8 son 1,2,4 cuya suma es 7 distinto de 10.
'''

def sumaDivisores(n):
    suma = 1
    for i in range(2,n):
        if n % i == 0:
            suma = suma + i
    return suma

def sonAmigos(n1,n2):
    sumaDivN1 = sumaDivisores(n1)
    sumaDivN2 = sumaDivisores(n2)
    
    if sumaDivN1 == n2 and sumaDivN2 == n1:
        return True
    else:
        return False
    

for i in range(100,300):
    for j in range(100,300):
        if sonAmigos(i,j):
           print("Son amigos ", i, ' - ' , j) 


