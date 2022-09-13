# -*- coding: utf-8 -*-
#
##Reto #5 - Calcular volumen de un cilindro
#Pide a tu usuario que indique el radio y la profundidad de un cilindro.
#Después aplica la fórmula correspondiente para calcular el volumen del cilindro
#y reduce el resultado a un solo decimal.
import math

if __name__ == '__main__':
    radio = float(raw_input("ingrese el radio: "))
    profundidad = float(raw_input("ingrese la profundidad: "))

    volumen=math.pi*radio**2*profundidad
    print("el volumen es : %.1f" % volumen)
