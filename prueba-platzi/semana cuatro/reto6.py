# -*- coding: utf-8 -*-
#
# Reto #6 - Mostrar enteros y residuos
#Pide al usuario que ingrese 2 números, divídelos,
#muestra un resultado como enteros y además el residuo por separado de una forma
#que seal fácil de entender al usuario.
#Por ejemplo: “9 dividido entre 2 es 4 y sobra 1”.


if __name__ == '__main__':
    numero_uno = int(raw_input("ingrese el numero uno: "))
    numero_dos = int(raw_input("ingrese la numero dos: "))

    division = numero_uno / numero_dos
    residuo = numero_uno % numero_dos

    print("{} dividido entre {} es {} y sobra {}".format(numero_uno, numero_dos, division, residuo))
