# -*- coding: utf-8 -*-
#
# Reto #4 - Calcular área de un círculo
#Solicita a tu usuario que ingrese un número el cual será el radio de un círculo
# y con este dato calcula el área de un círculo.
#Si tu lenguaje cuenta con librerías específicas para este propósito haz uso de las mismas.

import math
if __name__ == '__main__':
    radio_circulo = int(raw_input("ingrese el radio del circulo: "))
    area = math.pi*radio_circulo**2
    print('el area del circulo es %.3f ' % area)
