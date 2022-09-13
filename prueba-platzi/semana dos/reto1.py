# -*- coding: utf-8 -*-
#Reto #1 - Número mayor y menor
#Escribe un programa que pida al usuario 2 números,
#mostrando como salida cuál es el número mayor y la diferencia de uno respecto al otro.
#En caso de que los números sean iguales,
#mostrarlo también en pantalla.

def validar_numero(a, b):
    acum = 0
    if a == b :
         print('los numeros son igual')
    if a > b:
        acum = a - b
        print('{} es mayor que {} y la diferencia es {}'.format(a, b, acum))
    if b > a:
        acum = b - a
        print('{} es mayor que {} y la diferencia es {}'.format(b, a, acum))


if __name__ == '__main__':
    numero_1 = int(raw_input("ingrese el numero uno: "))
    numero_2 = int(raw_input("ingrese el numero dos: "))
    validar_numero(numero_1, numero_2)
