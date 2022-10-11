'''
5. Escriba una función que devuelva la media o promedio de dos números solicitados al
usuario.
'''
def promedio(a, b):
  rpta = ( a + b ) / 2

  return rpta

# PRograma principal
a = int(input("Ingresar A "))
b = int(input("Ingresar B "))

rpta = promedio(a,b)
print("El promedio es ", rpta)

