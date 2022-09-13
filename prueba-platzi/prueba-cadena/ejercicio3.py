# -*- coding: utf-8 -*-

# 3.	Generar un algoritmo que permita determinar el número de CDs vírgenes que se requieren
# para hacer la copia de seguridad de un disco duro del cual se conoce el tamaño.
# El algoritmo debe considerar las siguientes condiciones:

# •	El usuario debe ingresar el tamaño del disco duro en gigabytes (GB)
# •	Se usarán CDs de 700 megabytes (MB) de capacidad
# •	Un gigabyte es igual 1024 megabytes

import math
import sys

def convertir_gigas_megas(tam_disco_duro):
    return (tam_disco_duro * 1024)

def convertir_megas_cds(tam_disco_duro):
    return (math.ceil(convertir_gigas_megas(tam_disco_duro) / 700))


def main():
    tam_disco_duro = int(input("ingrese la capacidad del disco duro en gigabytes : "))

    print("""
        el numero de cds virgenes que se necesitan para sacar la copia de
        seguridad de un disco del tamaño de {} GB es de {} cds
        """
    .format(tam_disco_duro, convertir_megas_cds(tam_disco_duro)))


if __name__ == '__main__':
    while True:
        menu =int(input('''
        escoge una opcion:
            [1] CALCULAR CDs
            [2] SALIR
        '''))
        if menu == 1:
            main()
        if menu == 2:
            sys.exit()
