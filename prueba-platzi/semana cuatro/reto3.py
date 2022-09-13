# -*- coding: utf-8 -*-
#
# Reto #3 - Raíces cuadradas redondeadas
#Pide a tu usuario que ingrese un número, cuyo valor debe ser mayor a 20,
#luego calcula su raíz cuadrada y reduce a 2 o 3 decimales el resultado final.

import math


if __name__ == '__main__':
    numero = float(raw_input("ingrese un numero mayor a 20 : "))
    if numero >= 20:
        resultado = round(math.sqrt(numero), 2)
        print("la raiz cuadrada es : {}".format(resultado))
    else:
        print("digite un numero mayor a 20")
