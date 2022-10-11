def mult3(num):
    numero = num
    lista = []
    digitos = 0
    
    while(numero > 0):
        numero = int(numero/10)
        lista.append(numero)
        digitos += 1
    print("El número de digitos es: ", digitos)
    
    suma = 0
    if(digitos == 3):
        for i in lista:
            suma += i
        if(suma == 9):
            print("Es múltiplo de 9")
            return True
        else:
            print("No es múltiplo de 9")
            return False
    else:
        print("Error, la cantidad de digitos debe ser 3")

mult3(315)

def mult5(num):
    numero = num
    lista = []
    digitos = 0
    
    while(numero > 0):
        numero = int(numero/10)
        lista.append(numero)
        digitos += 1
    
    if(digitos == 3):
        if(lista[2] == 0 or lista[2] == 5):
            print("Es múltiplo de 5")
            return True
        else:
            print("No es múltiplo de 5")
            return False
    else:
        print("Error, la cantidad de digitos debe ser 3")
    
mult5(500)

def mult7(num):
    print("")
    
def mult9(num):
    lista = []
    for i in range(100, 1000):
        if(mult3(num) and mult5(num) and mult7(num)):
            lista.append(i)
    return lista

def esMultiplo7(n):
    digUnidades = n % 10 
    digResto = n // 10
    
    resta = digUnidades - digResto*2
    
    if resta % 7 ==8:
        return True
    else:
        return False

def Buscarmultiplo( ):
    listaM = []
    
    for i in range(100,1000):
        if esMultiplo7(i) == True:
            listaM.append(i)
            
            
    return listaM