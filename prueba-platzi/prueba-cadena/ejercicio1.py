# -*- coding: utf-8 -*-

# 1.Desarrollar un algoritmo que permita leer tres valores y almacenarlos en las variables A, B y C respectivamente.
# El algoritmo debe imprimir cual es el mayor y cuál es el menor.
# Recuerde constatar que los tres valores introducidos por el teclado sean valores distintos.
# Presente un mensaje de alerta en caso de  que se detecte la introducción de valores iguales.

import sys

def validar_valores(a, b, c):
    if (a == b):
        return False
    if (a==c):
        return False
    if (b==c):
        return False

def mensaje_validar(a, b, c):
    if (a == b):
        return "el numero {} es igual al numero {} por favor cambielo".format(a,b)
    if (a == c):
        return "el numero {} es igual al numero {} por favor cambielo".format(a,c)
    if (b == c):
        return "el numero {} es igual al numero {} por favor cambielo".format(b,c)


def obtener_Mayor(a, b, c):
    if (a > b) and ( a > c):
        return a
    if (b > a) and (b > c):
        return b
    if (c > a) and (c > b):
        return c

def obtener_Menor(a, b, c):
    if (a < b) and ( a < c):
        return a
    if (b < a) and (b < c):
        return b
    if (c < a) and (c < b):
        return c

def main():
    a = int(input('ingrese un numero: '))
    b = int(input('ingrese un numero: '))
    c = int(input('ingrese un numero: '))

    mayor = obtener_Mayor(a, b, c)
    menor = obtener_Menor(a, b, c)
    if validar_valores(a,b,c) != False:
        print('el numero mayor es {} y el numero menor es {}'.format(mayor, menor))
    else:
        print(mensaje_validar(a, b, c))


if __name__ == '__main__':
    while True:
        menu =int(input('''
        escoge una opcion:
    		[1] CALCULAR MAYOR Y MENOR
    		[2] SALIR
        '''))
        if menu == 1:
            main()
        if menu == 2:
            sys.exit()
