def main:
    
Num = Ingresar numero

if num >0
    cifra uno =  num % 10
    num = num / 10

    cifra dos = num % 10
    num = num / 10
   
    cifra tres = num

    suma cifras =  cifra uno +  cifra dos + cifra tres

    if suma cifras % 9 == 0
         Mostrar el número ingresado es múltiplo de 11
    else
         Mostrar que el numero ingresado no es múltiplo de 11
    else
         Mostrar que el numero ingresado no es válido



def imprimir_submultiplos(11):
    for i in range(1, 11+1):
        if es_multiplo(11, i):
            print(f"{i},", end=""