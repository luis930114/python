# -*- coding: utf-8 -*-
#Reto #3 - Rangos cambiantes.
#Nuevamente pide a tu usuario que indique 3 números: un límite superior,
#un límite inferior y uno de comparación.
#Si el número de comparación se encuentra entre los 2 primeros,
#comunicarlo en pantalla. En caso estar por debajo del límite inferior o por arriba del límite superior,
#también mostrarlo en pantalla.
#
def comparar_limite(inferior, superior, comparacion):
    if (comparacion >= inferior) and (comparacion <= superior):
        print('el numero {} se encuentra en el rango, gracias'.format(comparacion))
    else:
        print('el numero {} no esta en el limite permitido'.format(comparacion))

if __name__ == '__main__':
    limite_inferior = int(raw_input("ingrese el  limite inferior: "))
    limite_superior = int(raw_input("ingrese el limite superior: "))
    numero_comparacion = int(raw_input("ingrese un numero: "))

    comparar_limite(limite_inferior, limite_superior, numero_comparacion)
