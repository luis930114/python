# -*- coding: utf-8 -*-
#
# Reto #7 - Calcular perímetros y áreas
#Muestra un menú con distintas figuras geométricas,
#por lo menos 3 diferentes (triángulo, cuadrado, pentágono, etc.)
#Tu usuario debe poder elegir alguna de estas figuras,
#indicar la distancia de sus lados y mostrar como resultado tanto el perímetro
#como el área de dicha figura.
#
import math
import sys
menu = {
    "triangulo": '''
                1
               1 1
              1 1 1
             1 1 1 1
            1 1 1 1 1
    ''',
    "cuadrado":'''
            1 1 1 1 1
            1       1
            1 1 1 1 1
    ''',
    "circulo": '''
                111111111
               1         1
              1           1
              1            1
               1          1
                111111111
    '''
}
def main():
    figura =int(raw_input('''
    escoge una figura:
		[1] TRIANGULO
		[2]	cuadrado
		[3]	circulo
		[4] SALIR
    '''))
    if figura == 1:
        lado_1 = int(raw_input("ingresa la distancia del lado 1"))
        lado_2 = int(raw_input("ingresa la distancia del lado 2"))
        lado_3 = int(raw_input("ingresa la distancia del lado 3"))
        perimetro = lado_1 * lado_2 * lado_3
        base = int(raw_input("ingresa la base: "))
        altura = int(raw_input("ingresa la altura: "))
        area = (base * altura)/2
    if figura == 2:
        lado_1 = int(raw_input("ingresa la distancia de los lados: "))

        perimetro = lado_1 * 4

        area = lado_1 ** 2
    if figura == 3:
        radio = int(raw_input("ingresa la distancia del radio"))
        perimetro = 2 * math.pi() * radio
        area = area = math.pi*radio_circulo**2
    if figura == 4:
        sys.exit()
    print("area : {} y el perimetro: {}".format(area, perimetro))



if __name__ == '__main__':
    while True:
        main()
