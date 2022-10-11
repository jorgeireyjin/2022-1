'''Implemente una función que reciba dos números enteros a y b, y calcule el resultado de ab
utilizando operaciones de multiplicación. Tome en cuenta que tanto a como b también
podrían tomar valores negativos
'''
def elevar(a, b):
  rpta = 1
  if b >= 0:
    for i in range(1,b+1):
      rpta = rpta*a
  else:
    b = b* -1
    for i in range(1,b+1):
      rpta = rpta*a
    rpta = 1 / rpta
  
  return rpta

# PRograma principal
a = int(input("Ingresar A "))
b = int(input("Ingresar B "))

rpta = elevar(a,b)
print("La rpta es ", rpta)
